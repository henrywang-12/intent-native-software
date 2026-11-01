# 7. Interoperability has four layers


Two agents can exchange valid messages and still fail to cooperate. One may interpret a deadline as local time, another as UTC. One may accept a request as tentative, another as binding. A shared wire format does not settle those differences.

Distinguish four layers: transport, meaning, authority and commerce. Transport moves messages. Meaning establishes compatible units, entities and postconditions. Authority determines who may do what. Commerce establishes who pays, who carries risk and how disagreements are resolved. An ecosystem can be open at one layer and restrictive at another.

MCP provides a concrete host-client-server architecture for connecting tools and context. A2A's launch addresses coordination between independently built agents. They are relevant building blocks, not evidence that every service can already be composed safely. [S06: MCP architecture, 2025-06-18 specification](https://modelcontextprotocol.io/specification/2025-06-18/architecture) [S05: Announcing the Agent2Agent Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)

A capability directory therefore needs more than a natural-language description. Useful metadata includes versioned schemas, effect classes, authentication requirements, evidence endpoints, failure modes and geographic or business constraints. Discovery quality should be measured by whether the selected capability satisfies the task, not whether its description sounds relevant.

Semantic portability can be tested with a substitution experiment. Replace provider A with provider B while keeping the user's goal constant. Record which fields, policies, assumptions and recovery paths must change. A low adapter count is impressive only if the new workflow preserves its meaning.

There is an economic tradeoff. Rich standards reduce repeated negotiation but impose implementation costs and may freeze imperfect abstractions. Thin standards spread more easily but leave significant integration work to hosts. A promising platform exposes a minimal common contract and keeps domain-specific obligations explicit.

The important prediction is not that one protocol will own the internet. It is that the cost of joining a useful execution network becomes measurable and strategically important. If that cost falls sufficiently, independent services gain an alternative to rebuilding themselves inside every host.
