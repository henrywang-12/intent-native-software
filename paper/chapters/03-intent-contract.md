# 3. From language to an executable contract


An instruction is usually incomplete. “Find somewhere for Friday” leaves unresolved the participants, time, budget and whether the user wants a suggestion or a commitment. Treating fluent interpretation as authorization makes uncertainty invisible at the most consequential moment.

Represent an interpreted intent as I = (G, C, A, E): a goal predicate G, constraints C, delegated authority A and required evidence E. This is a modeling choice for the study, not a new standard. The components separate questions that a chat message compresses into one sentence.

For an illustrative booking, G means a confirmed reservation exists; C includes the date and party size; A allows searching but may require explicit approval for commitment; E is an authoritative provider record matching the approved request. “The tool returned success” satisfies none of these conditions by itself.

A capability contract K = (X, Y, P, Q, F, V) records input and output types, preconditions, postconditions, declared effects and version. Structural validation checks X and Y. Domain validation checks meanings such as currency, timezone and recipient identity. Authorization checks whether the current principal may produce F under this request. Verification checks whether evidence supports Q.

The contract should also expose uncertainty: unavailable, rejected, pending and indeterminate outcomes require different recovery. Converting them all to an exception string gives the planner too little information to act responsibly.

A worked example makes the boundary concrete. A person asks an assistant to reserve a meeting room and invite four colleagues. The assistant proposes a room at a stated price, obtains an exact approval and dispatches the reservation. The response is lost. It does not book a second room: the task becomes indeterminate until an authoritative lookup confirms the first reservation. Only then does it draft invitations. If the room is unavailable, a more expensive alternative requires new approval. If an invitation fails after the booking succeeds, the system reports partial completion; cancellation is a new decision with its own fee and authority. The provider benefits from fewer duplicate requests, while the user benefits only if checking and recovery cost less than the original manual process.

The difficult research question is how much contract work pays for itself. A perfectly described capability that nobody maintains is worse than a stable conventional integration. We therefore propose measuring authoring and maintenance time per verified task, including semantic changes and broken versions. The thesis loses force if contract overhead exceeds the saved coordination cost.

The public demo provides one small implementation of exact-request approval and evidence checking. It has no language-model interpretation stage; that boundary is deliberate, and it prevents its deterministic results from being mistaken for agent intelligence. [S28: Intent-Native Software: public execution demo](https://github.com/henrywang-12/intent-native-software/tree/4a984b552067bcc141d18052d304a08f6111ab52/demo)
