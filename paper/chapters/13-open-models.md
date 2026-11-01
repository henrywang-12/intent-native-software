# 13. Open models change bargaining power, not every bottleneck


Open weights can give a software operator more choices about deployment, customization and provider dependence. They do not automatically provide inexpensive serving, training reproducibility, usable data rights or access to external services.

The Open Source Initiative's definition treats code, parameters, data information and freedoms together. We therefore distinguish open weights from a verified claim of open-source AI under that definition. [S20: The Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)

DeepSeek-R1's report and the Qwen3 report illustrate mechanisms by which reasoning methods, smaller models and configurable inference can broaden the set of usable model choices. They are historical technical examples, not claims about the latest leading model. [S16: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/html/2501.12948v1) [S17: Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)

Consider bargaining between a service platform and its model supplier. A credible ability to switch can limit dependence even if switching never occurs. But credibility requires more than a compatible API: the replacement must preserve task quality, latency, policy behavior and operational support at an acceptable cost.

Now consider bargaining between the platform and its users. Replacing the model does little to help a user leave if their history, provider relationships and delegation state remain trapped. Model openness and ecosystem openness are separate variables.

This creates two plausible futures. Competitive models can support many interoperable service networks. Alternatively, commoditized models can strengthen a few gateways that control demand and scarce integrations. Open weights do not logically select between those futures.

The strongest implementation strategy is to preserve substitution at several layers: model, provider, interface and exported task state. Each substitution should be tested independently. A product that claims portability should demonstrate a successful exit, not merely publish a schema.

For a new entrant, open models may lower the cost of experimentation. The durable opportunity remains solving a recurring user problem with dependable operations. A downloadable model is an input to that business, not the business itself.
