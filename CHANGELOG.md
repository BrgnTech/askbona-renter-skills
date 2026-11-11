# Changelog

What changed in each version of the Bona renter guide, and why. Newest first.

## 0.4.1 · November 11, 2026

**In short:** the message you send first now carries Bona's key rules, so you get Bona's answer even when your assistant does not follow the full guide.

### Changed

- **A stronger start message.** It now sets out the one reply for a shared listing (the read, the cost so far, the questions, and what to check in person), the exact-question rules and limits, no numbers from memory, no unasked negotiation advice, and no legal answers. It also asks the assistant to say in one line if the guide's full text is not in the chat. *Why:* in ChatGPT, the old one-paragraph message was the part the assistant followed most. Given only a link to the guide, ChatGPT acted as if it had read it, answered from general knowledge, and suggested a rent figure nobody had offered.
- **Links to the guide.** The guide and the README now say plainly that a link is less reliable than attaching the file or pasting the text.

### Tested

In ChatGPT without an account, on the free model, one run each. With the old message, a link to the guide produced a generic checklist of about thirty questions, and pasted text produced seventeen. With the new message, three chats (no guide, a link, and pasted text) each gave the one reply for a shared listing, eight tour questions, no unasked negotiation advice, and no invented figures. Two of the three gave no summary of the law on a voucher question; one added a sentence about a state rule. Signed-in accounts, paid models, and other assistants have not been tested. See [Limitations](LIMITATIONS.md).

## 0.4.0 · November 10, 2026

**In short:** share a listing and Bona answers in one clear reply, with exact questions to ask the property. It sounds more like a friend who knows renting, and it stays out of legal conclusions and guessed numbers.

### Added

- **Exact questions.** Every question Bona writes names the home, asks for an answer that settles it (a dollar figure, a yes or no, a date, or hours), and asks for it in writing. Bona also tells you which replies would leave the question open, and gives one polite follow-up. *Why:* “Are there any fees?” is easy to answer without saying anything. “What does parking cost per month for unit 214, in dollars, and is it required?” is not.
- **One reply when you share a home.** Paste a listing, a screenshot, or page text and you get one answer: Bona's read, the cost so far, the questions to ask, and what to check in person. *Why:* before, the answer you got depended on how you phrased the request.
- **A list to carry to the tour.** Questions on fees, specials, and repairs, plus what to get in writing before you leave.
- **Features become questions.** Bona picks the features on the page that matter to you (a pool, parking, “pet friendly,” a smart home package) and turns each into a question about cost, limits, or condition. *Why:* a page shows features far more often than it shows what they cost.
- **Kinds of home.** Different questions for an apartment community, student housing, a house or private owner, an income-restricted home, and a room or sublet. *Why:* a per-bed student lease and a house from a private owner leave different things open, and the guide used to assume every home was an apartment community.

### Changed

- **A plainer, warmer voice.** Bona gives a verdict and the fact it rests on, keeps replies short, and asks at most one question at a time. It stays polite and exact with property staff.
- **Links.** If your assistant can't open a link, Bona says so and asks for the page text or a screenshot. It never describes a page it did not read.
- **Legal questions.** Bona explains what a supplied lease or quote says. It does not say what the law permits or requires. It tells you what to ask and which kind of office can answer. *Why:* in test chats before this change, assistants sometimes answered a legal question from memory.
- **Numbers.** Dollar amounts, deadlines, and screening cutoffs come only from the page, from you, or from a written reply. *Why:* in test chats before this change, an assistant supplied typical fee ranges that were not on the page.
- **Listing and review sites** are no longer named in Bona's answers or drafts.

### Tested

AI assistants followed the guide through thirteen fictional renter chats in developer tools. It has not been tested in consumer apps such as ChatGPT or Claude, or with a real leasing team. See [Limitations](LIMITATIONS.md).

## 0.3.0 · October 30, 2026

First public release: one coordinator and nine specialist skills, the complete guide in one file (`BONA.md`), and index files that help AI tools find the skills.
