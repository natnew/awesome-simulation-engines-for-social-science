# Awesome Simulation Engines for Social Science

A curated research and engineering map for AI-driven social simulation, synthetic populations, agent-based modelling, policy experiments, uncertainty modelling, and ethical risk discovery.

Social systems are adaptive, uncertain, partially observable, and non-linear. This repository maps the methods, systems, datasets, frameworks, and evaluation practices needed to explore possible futures under different interventions.

## Resource Map

| Section | What it contributes to the engine |
|---|---|
| [Computational Social Science](#computational-social-science) | Field foundations, methods, and policy-relevant applications |
| [Complex Systems](#complex-systems) | Emergence, feedback loops, non-linearity, and adaptation |
| [Social Simulation](#social-simulation) | Methodology, history, and landmark simulation systems |
| [Microsimulation](#microsimulation) | Population-level policy modelling and distributional analysis |
| [Causal Inference](#causal-inference) | Intervention reasoning and counterfactual logic |
| [Uncertainty Quantification](#uncertainty-quantification) | Probability landscapes rather than single predictions |
| [Responsible AI](#responsible-ai) | Risk surfacing, bias, governance, and ethical design |
| [Existing Systems](#existing-systems) | End-to-end simulation platforms already in use |
| [Agent-Based Modelling](#agent-based-modelling) | Micro-level behavioural simulation frameworks and protocols |
| [Synthetic Populations](#synthetic-populations) | Population construction and demographic realism |
| [Multi-Agent Reinforcement Learning](#multi-agent-reinforcement-learning) | Strategic interaction, cooperation, competition, and adaptation |
| [LLM-Based Social Simulation](#llm-based-social-simulation) | Generative agents, LLM societies, and language-mediated behaviour |
| [Machine-Learned World Models](#machine-learned-world-models) | Learned simulation dynamics and latent environment models |
| [Policy and Intervention Modelling](#policy-and-intervention-modelling) | Governance, decision-support, and policy experiment examples |
| [Ethical Risk Discovery](#ethical-risk-discovery) | Second-order harms, distributional risk, and misuse pathways |
| [Datasets and Empirical Grounding](#datasets-and-empirical-grounding) | Empirical grounding for synthetic societies and calibration |
| [Tools and Libraries](#tools-and-libraries) | Practical libraries for the full simulation stack |
| [Benchmarks and Testbeds](#benchmarks-and-testbeds) | Evaluation environments for agent behaviour and social dynamics |

## Why this exists

The Social-science Simulation Engine is an AI-native tool for modelling emergent human systems under uncertainty. This repository maps the research, methods, and engineering practices needed to build simulation engines that can hold that complexity — and to help others build them too.

## Resources

### Computational Social Science

- [Lazer et al. — Computational Social Science: Obstacles and Opportunities (2020)](https://www.science.org/doi/10.1126/science.aaz8170) `paper` — A decade-on state-of-the-field assessment; identifies what large-scale simulation, observational data, and experimental design can now achieve and what structural barriers remain for policy-relevant CSS.
- [Gonzalez-Bailon et al. — Computational Social Science and Sociology (2020)](https://www.annualreviews.org/content/journals/10.1146/annurev-soc-121919-054621) `paper` — Maps how computational methods — including simulation — are reshaping sociology; a practical orientation to the field for researchers building social engines.
- [Bail, C. — Breaking the Social Media Prism (2021)](https://press.princeton.edu/books/hardcover/9780691203423/breaking-the-social-media-prism) `book` — Uses large-scale social simulation experiments to test theories of political polarisation; a worked example of CSS methods applied to a real policy-relevant question.

### Complex Systems

- [Mitchell, M. — Complexity: A Guided Tour (2009)](https://academic.oup.com/book/51004) `book` — The clearest single-volume primer on emergence, feedback loops, adaptation, and self-organisation; the conceptual foundation for understanding why social simulation engines behave the way they do.
- [Aeon — Complex systems science allows us to see new paths forward (2024)](https://aeon.co/essays/complex-systems-science-allows-us-to-see-new-paths-forward) `article` — Connects complex systems thinking to contemporary social challenges including pandemics and inequality; explains why non-linearity and emergence make single-point predictions insufficient.
- [Farmer et al. — Nature — Economics needs a scientific revolution (2009)](https://www.nature.com/articles/460182a) `paper` — Argues that agent-based simulation engines are the right tool for economics precisely because social systems are complex and adaptive; a direct intellectual ancestor of the simulation engine concept.

### Social Simulation

- [Park et al. — Generative Agents: Interactive Simulacra of Human Behavior (2023)](https://dl.acm.org/doi/fullHtml/10.1145/3586183.3606763) `paper` — The landmark paper demonstrating LLM-driven agents that wake up, form relationships, and coordinate events in a simulated town; the most-cited recent example of a working social simulation engine.
- [Gao et al. — AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents (2025)](https://arxiv.org/abs/2502.08691) `paper` — Proposes a large-scale social simulator with a dedicated simulation engine, realistic societal environment, and 10,000+ LLM-driven agents; directly demonstrates the architecture this repo maps toward.
- [Nature — The first 'AI societies' are taking shape (2025)](https://www.nature.com/articles/d41586-026-00070-5) `article` — A Nature news feature surveying the emerging landscape of AI-powered social simulation engines and the scientific and ethical questions they raise.

### Microsimulation

- [EUROMOD — Tax-Benefit Microsimulation Model for the EU](https://euromod-web.jrc.ec.europa.eu/overview/what-is-euromod) `tool` — The reference implementation of policy microsimulation at scale; models tax and benefit rules across EU member states to estimate distributional effects of policy changes on household incomes.
- [Katikireddi et al. — Microsimulation as a flexible tool to evaluate policies and their impact on socioeconomic inequalities in health (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10590730/) `paper` — Demonstrates how a microsimulation engine surfaces unequal health effects of policy interventions across income and demographic groups — a direct example of the distributional analysis this engine aims to support.
- [Lovelace et al. — A Large-Scale Geographically Explicit Synthetic Population with Social Networks for the United States (2024)](https://www.nature.com/articles/s41597-024-03970-1) `paper` — Builds a country-scale synthetic population with embedded social networks for agent-based and microsimulation use; shows the current state of the art in population engine construction.

### Causal Inference

- [Hernán, M.A. & Robins, J.M. — Causal Inference: What If (2023)](https://miguelhernan.org/whatifbook/) `book` — The definitive free textbook on causal inference using potential outcomes; covers counterfactual reasoning and intervention analysis directly applicable to simulation engine design. Freely available online.
- [Kıcıman et al. — Causal Reasoning and Large Language Models: Opening a New Frontier for Causality (2023)](https://arxiv.org/abs/2305.00050) `paper` — Evaluates whether LLMs can support causal reasoning in simulation contexts; directly relevant to building intervention layers in LLM-augmented social engines.
- [Nilforoshan et al. — Language Models as Scientist and Subjects (2024)](https://arxiv.org/abs/2404.11794) `paper` — Uses structural causal models combined with LLMs to automatically generate and test social scientific hypotheses in silico; a working example of causal simulation engine methodology.

### Uncertainty Quantification

- [Kahn et al. — Uncertainty Quantification for Agent-Based Models (2024)](https://arxiv.org/html/2409.16776) `paper` — Applies Gaussian processes, sequential design, and history matching to quantify uncertainty in ABM outputs; the current state of the art for making social simulation engines produce calibrated rather than overconfident results.
- [Salter et al. — Improving Policy-Oriented Agent-Based Modeling with History Matching (2025)](https://arxiv.org/abs/2501.00616) `paper` — Demonstrates history matching as a principled method for calibrating policy-oriented ABMs against real-world data; directly applicable to validating social simulation engines.
- [Saltelli et al. — Global Sensitivity Analysis: The Primer (2008)](https://publications.jrc.ec.europa.eu/repository/handle/JRC40639) `book` — The standard reference for sensitivity analysis of model outputs; explains how to identify which uncertain inputs drive output variance — still the foundational text for this capability.

### Responsible AI

- [Weidinger et al. — Sociotechnical Safety Evaluation of Generative AI Systems (2023)](https://arxiv.org/abs/2310.11986) `paper` — Proposes a framework for evaluating harms from generative AI systems across social, institutional, and individual dimensions; directly applicable to responsible design of LLM-driven simulation engines.
- [Obermeyer et al. — Dissecting Racial Bias in an Algorithm Used to Manage the Health of Populations (2019)](https://www.science.org/doi/10.1126/science.aax2342) `paper` — The canonical empirical demonstration that an AI system producing good aggregate outcomes can simultaneously produce severe distributional harm; the case study every simulation engine designer should know.
- [NIST — Artificial Intelligence Risk Management Framework (AI RMF 1.0) (2023)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) `framework` — The leading voluntary framework for managing AI risk across the full system lifecycle; covers trustworthiness, accountability, bias, and governance for AI-assisted policy and simulation tools.

### Existing Systems

*Coming soon.*

### Agent-Based Modelling

*Coming soon.*

### Synthetic Populations

*Coming soon.*

### Multi-Agent Reinforcement Learning

*Coming soon.*

### LLM-Based Social Simulation

*Coming soon.*

### Machine-Learned World Models

*Coming soon.*

### Policy and Intervention Modelling

*Coming soon.*

### Ethical Risk Discovery

*Coming soon.*

### Datasets and Empirical Grounding

*Coming soon.*

### Tools and Libraries

*Coming soon.*

### Benchmarks and Testbeds

*Coming soon.*

## Contributing

<p align="center">
  <img alt="We love Contributors" src="assets/We%20love%20Contributors%20%E2%80%94%20section%20title%20banner.png">
</p>

<p align="center">Thrilled to have you here.<br/>
Whether it's a quick typo fix, a fresh resource,<br/>
a doc polish, or a sweeping overhaul — every contribution helps this list grow.<br/>
Jump in and join the community — PRs of every size are welcome.</p>

<p align="center">📝 <a href="CONTRIBUTING.md">Read the contributing guide</a> · 🐛 <a href="https://github.com/natnew/awesome-simulation-engines-for-social-science/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22">good first issues</a></p>
