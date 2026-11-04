# One identity: continuity without universal exposure

*Platform power companion · 4 November 2026 · AI-assisted analytical working note.*

The useful promise of one online identity is continuity: the user can authenticate consistently, recover access and carry selected preferences across services. It should not mean that every provider receives the same permanent identifier or sees the user's entire history.

OpenID Connect defines an authentication layer and claims exchange, including pairwise subject identifiers. Authentication answers who is signing in within a specified relationship. It does not automatically grant an agent permission to buy, publish or disclose information.

**Design proposal.** Separate the user-facing account from service-specific identifiers, authorization grants and optional profile claims. A provider receives only the information necessary for the task. An agent gets a bounded grant, not the person's primary credential.

This creates a useful tension: continuity improves convenience while compartmentalization limits correlation and the consequences of compromise. The product should make both visible. Users need to know which services can identify them, which grants are active and what survives account disconnection.

**Proposed evaluation.** Compare onboarding completion, recovery success, unnecessary claims disclosure and cross-service account-linking risk. A reduction in login steps is not sufficient if recovery becomes more fragile.

**Falsifier.** If users must repeatedly reauthenticate because services cannot accept the shared identity, or if a central outage blocks essential tasks, the convenience claim is overstated. Identity is infrastructure whose quality includes graceful failure, not merely a fast happy path.

## Evidence boundary

- [OpenID Connect Core 1.0, errata set 2](https://openid.net/specs/openid-connect-core-1_0.html)

Source-backed observations are identified in the text. Mechanisms, designs and proposed tests are the author's analysis; none is an empirical result. Sources were accessed on 4 November 2026.
