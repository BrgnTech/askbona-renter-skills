#!/usr/bin/env python3
"""Build BONA.md and skills.json from skills/*/SKILL.md, or check them.

Usage:
    python3 scripts/build.py           # rewrite BONA.md and skills.json
    python3 scripts/build.py --check   # fail if either is stale or a local link is broken

Standard library only. No network access. Writes only the two generated files.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/BrgnTech/askbona-renter-skills"
RAW = "https://raw.githubusercontent.com/BrgnTech/askbona-renter-skills/main"
VERSION = "0.4.1"
DATE = "November 11, 2026"

# The coordinator first, then the specialists in the order a search usually runs.
ORDER = [
    "bona",
    "bona-understand-me",
    "bona-find-homes",
    "bona-work-out-costs",
    "bona-check-a-home",
    "bona-ask-before-a-tour",
    "bona-plan-tours",
    "bona-learn-from-tours",
    "bona-get-a-better-deal",
    "bona-choose-a-home",
]

HEADER = f"""# Bona: the complete renter guide

Version {VERSION}. {DATE}.

This guide combines the Bona coordinator and nine specialist workflows in one document. Give it to the AI assistant you already use and ask it to follow the guide. It does not override the assistant's own instructions, tool permissions, or your choices.

## To start

Attach this file or paste its contents into a new conversation. Then send the message below. It carries Bona's key rules, so it still helps if your assistant does not take in the whole guide.

```text
Use the Bona guide to help me rent a home and get a good deal. If the guide's full text is not in this chat, say so in one line, then follow the rules below anyway.

Start with my request and what I have already told you. Keep replies short. Answer what I asked, then stop. Save negotiation advice for when I ask. Ask me at most one question per reply, and only if my answer would change your next reply. Give me a clear recommendation when you can.

When I share a listing, reply in this order:
1. Your read: two or three sentences on whether you would tour it and the one thing I should not miss.
2. The cost so far, plus each charge or feature the page names without a price.
3. Questions for the property, by the rules below.
4. One to three things to check in person.

Questions for a property: three if I ask what you think, up to eight if I ask what to ask. Each asks for a dollar figure, a yes or no, a date, or hours, and asks for it in writing. Turn features on the page into questions: for a pool, whether it costs extra and what the hours are. Put the top three in one message I can send. Tell me which replies would leave a question open. When a reply misses the question, assume good faith, say what it left open, and draft one polite follow-up.

Use only numbers from the listing, from me, or from a written reply. Anything else stays unknown. In a message you draft for me, say only what I have told you about me and my plans. If I ask what the law allows, do not answer it or sum up the law. Give me the question to ask and the kind of office that can answer.
```

Then paste a listing or a screenshot of it, describe your search, or compare offers. No skill command is needed. If you share a link and your assistant cannot open it, paste the page text instead.

Results depend on your assistant. It must be able to read and follow a long set of instructions, and tools such as browsing vary by product and account. Attach the file or paste the text when you can. A link to the guide is less reliable: an assistant may open it without following it. The guide was tested in ChatGPT without an account; signed-in accounts, paid models, and other consumer assistants have not been tested.

Bona is a set of instructions, not a property service or a live listing feed. It does not send messages, book tours, or remember anything on its own. Cost and legal context is mainly from the United States, so check the rules where you live.

Copyright 2026 Bona. Public to read; no reuse license is granted. See {REPO}/blob/main/COPYRIGHT.md.

## Instructions for the assistant

Use the Bona coordinator below. Apply a specialist only when it helps answer the current request. Do not explain every workflow to the renter or make them complete all of them. These instructions work from supplied information when live tools are absent. Do not claim you browsed, made a file, contacted a property, booked a tour, or set up an alert unless you actually did.
"""

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def read_skill(name):
    path = ROOT / "skills" / name / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        raise SystemExit(f"{path}: missing frontmatter")
    meta = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    if meta.get("name") != name:
        raise SystemExit(f"{path}: name {meta.get('name')!r} does not match folder")
    if not meta.get("description"):
        raise SystemExit(f"{path}: missing description")
    if ": " in meta["description"]:
        raise SystemExit(f"{path}: description contains ': ', which breaks YAML frontmatter")
    return meta, text[match.end():]


def demote(body):
    """Move every Markdown heading down one level, leaving fenced code alone."""
    out, fenced = [], False
    for line in body.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and re.match(r"#{1,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out).strip("\n")


def build():
    skills = [(name, *read_skill(name)) for name in ORDER]
    guide = "\n\n---\n\n".join([HEADER.rstrip("\n")] + [demote(body) for _, _, body in skills]) + "\n"
    manifest = {
        "name": "bona-renter-skills",
        "version": VERSION,
        "description": "Instructions for a renter's own AI assistant: find a fitting home, understand the real cost, and move toward a sound lease.",
        "repository": REPO,
        "branch": "main",
        "completeGuide": {"path": "BONA.md", "url": f"{RAW}/BONA.md"},
        "rights": {"path": "COPYRIGHT.md", "url": f"{RAW}/COPYRIGHT.md"},
        "skills": [
            {
                "name": name,
                "description": meta["description"],
                "path": f"skills/{name}/SKILL.md",
                "url": f"{RAW}/skills/{name}/SKILL.md",
            }
            for name, meta, _ in skills
        ],
    }
    return {
        "BONA.md": guide,
        "skills.json": json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
    }


LINK = re.compile(r"""(?:\]\(|(?:src|srcset|href)=")([^)"\s#]+)""")
OWN_URL = re.compile(
    r"^(?:" + re.escape(RAW) + r"|" + re.escape(REPO) + r"/(?:blob|tree)/main)/(.+)$"
)


def broken_links():
    """Return links in public text files that point at a missing local file."""
    problems = []
    files = sorted(ROOT.glob("*.md")) + [ROOT / "llms.txt", ROOT / "skills.json"]
    files += sorted((ROOT / "skills").glob("*/SKILL.md"))
    for path in files:
        if not path.exists():
            problems.append(f"missing file {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        targets = LINK.findall(text) + re.findall(r'"(https://[^"]+)"', text)
        for target in targets:
            own = OWN_URL.match(target)
            if own:
                local = ROOT / own.group(1)
            elif re.match(r"^[a-z]+:", target):
                continue  # other external links are not checked offline
            else:
                local = (path.parent / target).resolve()
            if not local.exists():
                problems.append(f"{path.relative_to(ROOT)}: {target}")
    return problems


def main(argv):
    found = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
    if found != sorted(ORDER):
        raise SystemExit(f"skills/ folders {found} do not match ORDER")
    outputs = build()
    if argv == ["--check"]:
        stale = [n for n, text in outputs.items()
                 if not (ROOT / n).exists() or (ROOT / n).read_text(encoding="utf-8") != text]
        problems = [f"stale generated file {n}" for n in stale] + broken_links()
        changelog = ROOT / "CHANGELOG.md"
        lines = changelog.read_text(encoding="utf-8").splitlines() if changelog.exists() else []
        if f"## {VERSION} · {DATE}" not in lines:
            problems.append(f"CHANGELOG.md has no entry for {VERSION}")
        for problem in problems:
            print(problem)
        print("check failed" if problems else "check passed")
        return 1 if problems else 0
    if argv:
        raise SystemExit(__doc__)
    for name, text in outputs.items():
        (ROOT / name).write_text(text, encoding="utf-8")
        print(f"wrote {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
