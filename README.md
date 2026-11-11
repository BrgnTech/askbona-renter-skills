<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/logo.svg">
    <img src="assets/logo.svg" alt="Bona" width="220">
  </picture>
</p>

<h1 align="center">Bona renter skills</h1>

<p align="center">
  A calm, practical guide for the AI assistant you already use.<br>
  Find a home you want, understand what it really costs, and move forward with confidence.
</p>

<p align="center">
  <a href="https://github.com/BrgnTech/askbona-renter-skills/releases/latest/download/BONA.md"><strong>Download the guide</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="BONA.md"><strong>Read the guide</strong></a>
</p>

<br>

## Get started

1. **Download** [`BONA.md`](https://github.com/BrgnTech/askbona-renter-skills/releases/latest/download/BONA.md), the complete guide in one file.
2. **Open** a new chat in your AI assistant. Attach the file, or paste its contents.
3. **Send** the message below, then add your listing, quote, or question. It carries Bona's key rules, so it still helps if your assistant does not take in the whole guide.

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

Attach the file or paste the text when you can. A link to the guide is less reliable: an assistant may open it without following it.

## Things you can ask

> Here is a listing I'm touring on Saturday. What should I ask them?

> Here is a listing for a one-bedroom at $2,150. What will I really pay each month, and how much do I need on move-in day?

> I toured two places this weekend. The first was bright and quiet, but the second is ten minutes closer to work. Help me choose.

> They offered six weeks free on a 13-month lease, or lower rent on 12 months. Which is better, and can I ask for more?

You do not need to know which skill to use. Bona picks the useful one and starts from wherever you are.

## What is inside

One coordinator and nine specialists. They are capabilities, not steps you must complete.

| Stage | Skill | What you get |
| --- | --- | --- |
| **Start anywhere** | [Bona](skills/bona/SKILL.md) | The next useful step, without a long intake. |
| **Get clear and search** | [Understand me](skills/bona-understand-me/SKILL.md) | A short brief about what this move should improve. |
| | [Find homes](skills/bona-find-homes/SKILL.md) | A few distinct choices in one tidy list. |
| **Check a home** | [Work out costs](skills/bona-work-out-costs/SKILL.md) | Monthly cost, move-in cash, and the full lease cost. |
| | [Check a home](skills/bona-check-a-home/SKILL.md) | A closer look when something worries you. |
| | [Ask before a tour](skills/bona-ask-before-a-tour/SKILL.md) | Polite, exact questions for before and at the tour. |
| **Tour** | [Plan tours](skills/bona-plan-tours/SKILL.md) | A workable visit plan and a few personal checks. |
| | [Learn from tours](skills/bona-learn-from-tours/SKILL.md) | Better choices without repeating the interview. |
| **Decide** | [Get a better deal](skills/bona-get-a-better-deal/SKILL.md) | An honest request and a clear offer comparison. |
| | [Choose a home](skills/bona-choose-a-home/SKILL.md) | A recommendation and help with the next step. |

## Good to know

- **Bona is a set of instructions,** not a property service. It has no live listings and no connection to any property.
- **It does not act on its own.** It does not send messages, book tours, apply, pay, or remember anything. Any of that depends on your assistant's own tools and your say-so.
- **Results depend on your assistant.** It needs to read and follow a long document. Browsing and file tools vary by product and account.
- **Costs and rules are mainly US-based.** Check the rules where you live. This is not legal advice.
- **It is early.** It has been tried with fictional scenarios, but not tested end to end in consumer assistants. See [Limitations](LIMITATIONS.md).

## For agents and developers

Each skill is a standard [Agent Skills](https://agentskills.io/specification) folder at `skills/<name>/SKILL.md`. [`BONA.md`](BONA.md) combines all ten in one file. [`AGENTS.md`](AGENTS.md), [`llms.txt`](llms.txt), and [`skills.json`](skills.json) help agents find the right file.

To list the skills, or add them to the current project, with the [`skills`](https://github.com/vercel-labs/skills) command-line tool. The second command installs into the current project only.

```sh
npx skills add BrgnTech/askbona-renter-skills --list
```

```sh
npx skills add BrgnTech/askbona-renter-skills
```

The release also includes [`bona-renter-skills-v0.4.1.zip`](https://github.com/BrgnTech/askbona-renter-skills/releases/download/v0.4.1/bona-renter-skills-v0.4.1.zip). After editing a skill, run `python3 scripts/build.py` to rebuild the generated files, then `python3 scripts/build.py --check`.

Download and install links are provided for convenience. They do not grant a license to reuse or redistribute this material.

## What's new in 0.4.1

- **A stronger start message.** The message you send first now carries Bona's key rules: the one reply for a shared listing, exact questions, no guessed numbers, and no legal answers. In ChatGPT it kept that behavior with the guide attached, with only a link, and with no guide at all.

## New in 0.4.0

- **Exact questions.** Share a listing and get questions that ask for a dollar figure, a yes or no, or a date, in writing.
- **One clear reply.** Bona's read, the cost so far, what to ask, and what to check in person.
- **More kinds of home.** Student housing, a house from a private owner, income-restricted homes, and rooms or sublets.

See the [changelog](CHANGELOG.md) for what changed and why.

<br>

<p align="center">
  <sub>Version 0.4.1 · November 11, 2026 · © 2026 Bona · <a href="CHANGELOG.md">Changelog</a> · <a href="COPYRIGHT.md">Rights</a> · <a href="SOURCES.md">Sources</a> · <a href="LIMITATIONS.md">Limitations</a></sub>
</p>
