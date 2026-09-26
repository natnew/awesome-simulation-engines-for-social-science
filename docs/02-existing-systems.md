# Existing Systems

Working social simulation systems fall into a few recurring archetypes. This note describes them and says where each lives in the list, so it never duplicates the README's entries. The resources themselves, with links and one-line contributions, are in the [README](../README.md#resource-map).

## System archetypes

| Archetype | What it does | Where to look |
|---|---|---|
| Generative-agent societies | LLM-driven agents with memory, planning, and dialogue interacting in a shared environment | [Existing Systems](../README.md#existing-systems), [LLM-Based Social Simulation](../README.md#llm-based-social-simulation) |
| Agent-based modelling platforms | Rule-based agents on grids and networks, built for experiments and replication | [Agent-Based Modelling](../README.md#agent-based-modelling) |
| Economic and policy simulators | Environments where interventions or mechanisms are searched and compared | [Policy and Intervention Modelling](../README.md#policy-and-intervention-modelling), [Multi-Agent Reinforcement Learning](../README.md#multi-agent-reinforcement-learning) |
| Learned simulators | Dynamics learned from data rather than hand-coded, from latent world models to neural surrogates | [Machine-Learned World Models](../README.md#machine-learned-world-models), [Implementation Patterns](../README.md#implementation-patterns) |
| Population substrates | Synthetic populations and digital twins that the other archetypes run on | [Synthetic Populations](../README.md#synthetic-populations), [Datasets and Empirical Grounding](../README.md#datasets-and-empirical-grounding) |

## Questions to ask of any system

The [Functional lens](../README.md#functional-lens) gives six questions for judging a system, whatever its archetype:

1. **Reconstruct:** what observable social state does it produce, and from which data?
2. **Simulate:** which transitions and interactions does it model, and at what scale?
3. **Plan:** can it be used to choose interventions, and against which objectives?
4. **Calibrate:** how are its parameters fitted to data, and with what inference method?
5. **Validate:** what evidence shows its behaviour matches the system it represents?
6. **Risk:** which distributional harms, leakage, or misuse pathways has it been checked for?

Most published systems answer the first two well and the last three thinly. The [Uncertainty Quantification](../README.md#uncertainty-quantification), [Evaluation and Validation](../README.md#evaluation-and-validation), and [Ethical Risk Discovery](../README.md#ethical-risk-discovery) sections collect the methods for closing that gap.
