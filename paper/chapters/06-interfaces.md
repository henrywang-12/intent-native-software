# 6. The interface becomes a projection


If both humans and agents act on the same domain service, the interface need not be the service's sole identity. A task can appear as a conversation, a calendar, a table or a review screen while preserving the same underlying commitment.

This is not an argument for generating every screen. Stable layouts support spatial memory, comparison, expert speed and accessibility. A user selecting among many options may prefer a table to a long conversation. A generated interface is valuable when it reduces irrelevant navigation without making important state disappear.

The architectural rule is shared semantics. Changing the date through a form and changing it through conversation should invoke compatible validation and authorization. The agent must not have a hidden shortcut around the rules that constrain the visible product.

Human-AI interaction research emphasizes setting expectations and supporting correction when systems fail. These are useful design principles, but the quality of a particular interface still requires testing. [S23: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/)

Measure *comprehension after action*: can a person identify what changed, who received information, which future steps remain permitted and how to stop them? A system that reduces clicks while increasing misunderstandings has shifted work into a less visible place.

Persistent task objects also let interfaces specialize. A compact mobile view can show pending decisions; a desktop view can expose comparisons; an accessible text view can present the same commitments in sequence. The service keeps the authoritative state, while each projection offers a different way to reason about it.

The forecast is a weakening of the exclusive connection between an application and one primary interface. It does not require the disappearance of apps. The strongest version of intent-native software may combine conventional interfaces with agent coordination, letting people move between them without restarting their work.
