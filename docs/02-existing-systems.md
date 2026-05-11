# Existing Systems

The landscape of social simulation is populated by several state-of-the-art systems and frameworks that demonstrate the potential of AI-native modelling. These systems range from general-purpose generative agent libraries to domain-specific economic and urban simulators.

## Generative Agent Frameworks

These systems use Large Language Models (LLMs) to drive agent behaviour and interaction.

- **Concordia (Google DeepMind):** [GitHub](https://github.com/google-deepmind/concordia) | [Paper](https://arxiv.org/abs/2312.03664) — An open-source library for building LLM-driven multi-agent simulations grounded in physical, social, or digital environments.
- **Project Sid (Altera.AL):** [Paper](https://arxiv.org/abs/2411.00114) | [Website](https://altera.al/) — A large-scale simulation demonstrating emergent civilisational dynamics, including professions, governance, and cultural norms among hundreds of agents.
- **OASIS (Yang et al.):** [Paper](https://arxiv.org/abs/2411.11581) — A social media simulator capable of scaling to one million LLM-driven agents to study group behaviour and information propagation.

## Economic and Policy Simulators

Systems designed specifically for testing economic theories and policy interventions.

- **The AI Economist (Salesforce Research):** [Website](https://einstein.ai/the-ai-economist) | [Paper](https://www.science.org/doi/10.1126/sciadv.abk2607) — A two-level reinforcement learning framework where economic agents and a social planner co-adapt to design optimal taxation policies.
- **Stanford Economic Simulations:** [Project Page](https://digitaleconomy.stanford.edu/project/economic-simulations-with-ai/) — A research programme at the Stanford Digital Economy Lab that combines LLMs and causal reasoning to build auditable economic models.
- **PandemicSimulator (Sony AI):** [GitHub](https://github.com/SonyResearch/PandemicSimulator) | [Paper](https://www.jair.org/index.php/jair/article/view/12632) — An agent-based Markov model used to evaluate and optimise COVID-19 mitigation policies through reinforcement learning.

## Agent-Based Modelling (ABM) Platforms

Canonical frameworks for building bottom-up simulations of individual agents.

- **Mesa:** [GitHub](https://github.com/projectmesa/mesa) | [Website](https://mesa.readthedocs.io/) — The default Python-based ABM framework, widely used for its integration with the scientific Python stack.
- **NetLogo:** [Website](https://ccl.northwestern.edu/netlogo/) — The de-facto reference for emergence pedagogy and rapid prototyping of agent-based models.
- **AgentTorch:** [Paper](https://arxiv.org/abs/2409.10568) — A differentiable ABM framework from the MIT Media Lab that scales LLM-guided simulations to millions of agents.

## World Models and Learned Simulators

Systems that learn system dynamics directly from data rather than following hand-coded rules.

- **DreamerV3 (Google DeepMind):** [Paper](https://arxiv.org/abs/2301.04104) | [GitHub](https://github.com/danijar/dreamerv3) — A general-purpose world-model agent that learns to master diverse tasks by training inside its own learned latent-dynamics simulator.
- **GameNGen (Google Research):** [Paper](https://arxiv.org/abs/2408.14837) — A neural game engine that simulates interactive environments (like DOOM) using only diffusion models, without a traditional engine.
- **TrafficSim (Uber ATG):** [Paper](https://arxiv.org/abs/2101.06557) — A neural multi-agent traffic simulator that learns socially plausible driving behaviour from real-world logs.

## Synthetic Population Tools

Frameworks for constructing realistic populations that serve as the substrate for simulations.

- **Out of One, Many (Argyle et al.):** [Paper](https://doi.org/10.1017/pan.2023.2) — Foundational work demonstrating that LLMs can reproduce human survey response distributions when conditioned on demographic profiles.
- **CitySEIRCast:** [Paper](https://link.springer.com/article/10.1007/s40747-024-01683-x) — A city-scale digital twin that couples synthetic populations with mobility and social data for pandemic analysis.
- **Twin-2K-500:** [Dataset](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0262) — A dataset for building digital twins of over 2,000 people based on extensive psychological and behavioural measures.

## How this applies to this repository

These existing systems provide the **benchmarks and reference implementations** for the modular components we curate. By studying these platforms, we can identify the gaps in current simulation technology—such as the need for better uncertainty quantification or more transparent causal reasoning—and target our curation toward resources that address these needs.
