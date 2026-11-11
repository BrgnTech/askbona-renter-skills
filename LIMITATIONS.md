# Limitations

Bona is an early set of instructions. Read this before relying on it.

## What has been tried

The guide was exercised locally by AI assistants reading it against fictional renter requests. The requests covered organizing duplicate listings under a firm budget, comparing offers with credits and deposits, correcting lease terms that did not match a quote, and using an apartment quote to support a renewal request.

Those checks found and fixed an error in which a lease length was borrowed from a different home. A fresh check of that case then passed. Other cases were not rerun after that fix. These were a small number of local checks, not a reliability study.

For version 0.4.0, AI models from three vendors each followed the guide through the same fictional renter chats in developer tools, one run each. The chats covered a cold start, a student group, an amenity-heavy listing, a house from a private owner, poor credit, a renewal, a voucher question, a neighborhood question, a tour debrief, an application deadline, a link the assistant could not open, and a vague reply from a property.

A first pass on a draft found three problems. Two of the three models answered a legal question from memory. One supplied typical fee figures that were not on the page. Reply length for the same chats varied threefold. After the changes in 0.4.0, a second pass found no legal answer from memory and no figure from memory in any of the three runs. One model from the first pass was replaced in the second pass by another from the same vendor, so that result is not a like-for-like recheck. One model's replies were still much longer than the guide asks for. Small wording fixes followed the second pass.

For version 0.4.1, the guide was tried in ChatGPT on chatgpt.com without an account, on the free model, one run each. With the 0.4.0 start message, a link to the guide was not followed: ChatGPT acted as if it had read the guide, answered from general knowledge, and suggested a rent figure nobody had offered. With the guide text pasted in, it followed part of the guide. With the 0.4.1 start message, chats with no guide, with a link, and with pasted text each kept the main behavior: the one reply for a shared listing, eight tour questions, no unasked negotiation advice, and no invented figures. One of the three still added a sentence about a state law on a voucher question. On the tour list, none said which replies would leave a question open, and the assistant sometimes searched the web without being asked. Only two of the ten skills were pasted in that test.

These checks show how the wording reads to a model. They do not show how a consumer app behaves or how a real leasing team replies.

The packaging is also checked. The complete guide is rebuilt from the ten skill files, and local links are checked.

## What has not been tested

- **Consumer assistants.** Only ChatGPT without an account was tried. Signed-in accounts, paid models, attaching the file, plugin or skill installs, and other consumer products such as Claude have not been tested.
- **Opening a link.** An assistant may open a link to the guide without following it. Attaching the guide and pasting the page text is the safer route.
- **Real actions.** No messages, tours, applications, payments, alerts, or leases were created. Bona has no connection to any property, listing service, or calendar.
- **Real outcomes.** There is no evidence yet of savings, better choices, or completed rentals.
- **Replies to the questions.** Exact questions make a vague reply easy to spot. They cannot force anyone to answer. They are not legal advice and do not bind the property. No real leasing team has been asked them. A written reply is a record of what was said, so check that the lease says the same thing.
- **Local rules.** Cost and legal context is mainly from the United States. School, commute, accessibility, screening, legal, and emergency-housing questions need current local sources in a real case.

Your assistant may make mistakes, including with numbers. Check important figures and terms against the written offer or lease.
