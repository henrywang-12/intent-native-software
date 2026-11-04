# Portability is more than an identifier

*Platform power companion · 4 November 2026 · AI-assisted analytical working note.*

A stable identifier can survive a change of interface while the useful account remains trapped. Preferences, transaction history, reputation, entitlements and active tasks may all have different owners and export formats.

W3C DID Core describes an identifier architecture and associated verification methods. It does not guarantee universal acceptance, truthful claims, portable reputation or a right to transfer a commercial account. Different DID methods also make different operational assumptions.

**Proposal.** Define portability as a set of observable migration outcomes: the user can export necessary records, authenticate with a new client, reconnect eligible services and finish or safely cancel outstanding tasks. Migration should not require copying bearer tokens or private credentials into an archive.

Some attributes cannot be transferred as if they were ordinary files. A provider may need to reverify eligibility; a reputation score may depend on a specific marketplace's fraud model. Preserve evidence and provenance where appropriate instead of claiming a universal trust score.

**Experiment.** Move a synthetic user between two independent clients. Measure lost capabilities, repeated verification, time to resume tasks and data that cannot be interpreted. Include active disputes and pending payments.

**Counterargument.** Portability has implementation and abuse costs. Those costs should be measured against reduced switching friction. The relevant question is whether users can leave without disproportionate loss, not whether a protocol name sounds decentralized.

## Evidence boundary

- [W3C DID Core 1.0 (2022 recommendation)](https://www.w3.org/TR/2022/REC-did-core-20220719/)

Source-backed observations are identified in the text. Mechanisms, designs and proposed tests are the author's analysis; none is an empirical result. Sources were accessed on 4 November 2026.
