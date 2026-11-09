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
3. **Send** the prompt below, then add your listing, quote, or question.

```text
Use this Bona guide to help me find a home and get a good deal. Start with my request, use what I have already told you, and ask one useful question at a time. Give me a clear recommendation when you can.
```

If your assistant cannot open a link to the guide, attach the file or paste the text instead.

## Things you can ask

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
| | [Check a home](skills/bona-check-a-home/SKILL.md) | Why it may fit and what to resolve next. |
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

The release also includes [`bona-renter-skills-v0.3.0.zip`](https://github.com/BrgnTech/askbona-renter-skills/releases/download/v0.3.0/bona-renter-skills-v0.3.0.zip). After editing a skill, run `python3 scripts/build.py` to rebuild the generated files, then `python3 scripts/build.py --check`.

Download and install links are provided for convenience. They do not grant a license to reuse or redistribute this material.

<br>

<p align="center">
  <sub>Version 0.4.0 · November 9, 2026 · © 2026 Bona · <a href="COPYRIGHT.md">Rights</a> · <a href="SOURCES.md">Sources</a> · <a href="LIMITATIONS.md">Limitations</a></sub>
</p>
