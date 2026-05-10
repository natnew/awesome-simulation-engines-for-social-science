# Phase 11 — Ethical Risk Discovery: Research Notes

**Status:** Private — local only, never to be pushed or made public
**Date:** 2026-05-10

These notes record candidate research and editorial decisions that did not survive the cut into the canonical `### Ethical Risk Discovery` section of `README.md`. The README is authoritative; this file is only supplementary research context for future review passes (Phase 15 cross-cutting gaps and Phase 16 reference-architecture update).

---

## Methodology vs sub-area map

| Curated entry | Sub-area | Methodology | Source |
|---|---|---|---|
| Pan et al. 2023 (ICML, MACHIAVELLI) | Red-teaming / sociotechnical eval for generative-agent simulators | Annotated text-game benchmark for power-seeking, deception, ethical-violation eval of LM agents | UC Berkeley CHAI / Center for AI Safety |
| Ruan et al. 2024 (ICLR, ToolEmu) | Red-teaming / sociotechnical eval for generative-agent simulators | LM-emulated tool-execution sandbox + automatic safety evaluator for LM-agent risks | Stanford / Toronto |
| D'Amour et al. 2020 (FAccT, ML-fairness-gym) | Distributional-harm / fairness audit for learned-policy simulators | Simulation-based long-term fairness analysis + open-source gym | Google Research |
| Liu et al. 2018 (ICML, Delayed Impact) | Distributional-harm / fairness audit for learned-policy simulators | Forward-simulation of fairness-constrained policy effects on population state | UC Berkeley |
| Heidari et al. 2019 (ICML, Effort Unfairness) | Distributional-harm / fairness audit for learned-policy simulators | Simulation of effort-response social learning under deployed algorithmic policy | CMU / MPI-SWS |
| Stadler et al. 2022 (USENIX Security, Anonymisation Groundhog Day) | Misuse / dual-use / second-order harm for AI-native social simulation | Empirical privacy attacks (membership inference) on deep-generative synthetic populations | EPFL / Imperial College London |
| Park et al. 2024 (Patterns, AI Deception) | Misuse / dual-use / second-order harm for AI-native social simulation | Survey cataloguing learned deception by AI systems trained inside game / negotiation simulators | MIT / multi-lab |
| Solaiman et al. 2023 (Evaluating Social Impact of Generative AI) | Cross-cutting risk-discovery methodology | Categorical evaluation framework spanning base-system properties + societal-context evaluations | Hugging Face / Stanford / Allen AI / multi-lab |

---

## Candidates considered but not curated

### Group 1 — Red-teaming / sociotechnical eval for generative-agent / LLM-society simulators

- **Perez et al. 2022 *Red Teaming Language Models with Language Models* (EMNLP 2022).** DeepMind. Foundational generic-LLM red-teaming work; out of scope under the *simulation-engine-specific* boundary because the contribution is generic LLM red-teaming, not red-teaming applied specifically to a generative-agent simulator or LLM-society. Belongs in `### Responsible AI` consideration if that section is ever extended; not curated here.
- **Naihin et al. 2023 *Testing Language Model Agents Safely in the Wild* (NeurIPS 2023 SoLaR workshop).** Considered as a Group 1 entry on agent safety testing methodology. Deferred because the contribution is closer to single-agent AutoGPT-style sandboxing than to a generative-agent / LLM-society simulator, and ToolEmu (Ruan et al. 2024) is the stronger reference in the same line.
- **Mukobi et al. 2024 *Welfare Diplomacy: Benchmarking Language Model Cooperation* (NeurIPS 2024).** Strong candidate; uses Diplomacy as a benchmark for cooperative behaviour of LLM agents. Not curated to keep Group 1 at two entries and avoid overlap with the MACHIAVELLI text-game-benchmark line. Re-evaluate at Phase 14 (Benchmarks and Testbeds) where the benchmark framing is the right home.
- **Hua et al. 2024 *TrustAgent: Towards Safe and Trustworthy LLM-based Agents.*** Considered; deferred because the framework is not yet widely adopted and the safety-method contribution is incremental on top of ToolEmu.

### Group 2 — Distributional-harm / fairness audit for learned-policy simulators

- **Multi-Agent Multi-Objective RL for Climate Equity (arXiv 2505.01115).** Flagged in `docs/09-policy-and-intervention-modelling.md` as a Phase 11 candidate. Considered for Group 2; deferred because the closest fit is fairness-audit-via-simulation methodology and D'Amour 2020 + Liu 2018 + Heidari 2019 cover that ground with stronger canonical references. Re-evaluate at Phase 15 cross-cutting gaps where distributional-equity-via-MARL is the explicit theme.
- **Creager, Madras, Pitassi & Zemel — *Causal Modeling for Fairness in Dynamical Systems* (ICML 2020).** Strong candidate; uses causal models for fairness in dynamical systems. Not curated to avoid lineage saturation in the long-term-fairness-via-simulation line and because the causal-fairness methodology is closer to `### Causal Inference` than to a learned-policy audit. Re-evaluate at Phase 15.
- **Atwood et al. 2019 *Fair treatment allocations in social networks* (NeurIPS 2019).** Considered; deferred because the contribution is a single-domain (HIV-prevention treatment allocation) audit rather than a methodology a generic learned-policy audit would reuse.

### Group 3 — Misuse / dual-use / second-order harm for AI-native social simulation

- **Hayes, Melis, Danezis & De Cristofaro — *LOGAN: Membership Inference Attacks Against Generative Models* (PETS 2019).** Strong candidate on membership-inference attacks against generative models. Not curated because Stadler et al. 2022 is the stronger and more recent reference for the synthetic-population leakage risk specifically; LOGAN is the foundational substrate.
- **Carlini et al. *Membership Inference Attacks From First Principles* (S&P 2022).** Foundational substrate for membership-inference; out of scope under the *simulation-engine-specific* boundary because the contribution is generic membership-inference theory, not synthetic-population leakage. Cited as substrate via Stadler et al. 2022.
- **Sharma et al. *Towards Understanding Sycophancy in Language Models* (arXiv 2310.13548).** Anthropic. Considered for the *false-policy-authority* line; deferred because the contribution is generic LLM sycophancy, not policy-authority arising from a learned simulation engine. Belongs in `### Responsible AI` consideration if that section is ever extended; cited as substrate when an `### Ethical Risk Discovery` entry on false-policy-authority surfaces.
- **Burtell & Woodside *Artificial Influence: An Analysis Of AI-Driven Persuasion* (2023).** Considered for the influence-operations / dual-use line; deferred because the contribution is a non-research-lab analysis (Brookings / independent), not a research-lab methodology. Re-evaluate if an equivalent research-lab analysis surfaces.
- **AgentTorch / OASIS / Concordia *misuse / red-teaming follow-ups.*** None surfaced as a primary reference distinct from the simulators themselves (which are already in `### Agent-Based Modelling` / `### Existing Systems`). Re-evaluate at Phase 14 (Benchmarks) and Phase 15 (cross-cutting gaps).

### Group 4 — Cross-cutting risk-discovery methodology

- **Mökander, Schuett, Kirk & Floridi — *Auditing large language models: a three-layered approach* (AI Ethics 2023).** Oxford / GovAI. Strong candidate; proposes a three-layer governance / model / application audit framework. Not curated because the contribution is generic LLM auditing rather than a methodology the simulation engine's risk layer specifically reuses; closer to `### Responsible AI` boundary. Re-evaluate at Phase 13 (Tools and Libraries) if a consolidated audit-tooling section surfaces.
- **Raji et al. — *Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing* (FAT* 2020).** Google / Partnership on AI. Strong candidate; canonical end-to-end internal auditing framework. Not curated because the contribution is generic algorithmic auditing rather than risk-discovery for learned simulators specifically; Solaiman et al. 2023 is the stronger fit for the *categorical-framework-the-engine-reuses* slot.
- **Birhane, Prabhu & Kahembwe — *Multimodal datasets: misogyny, pornography, and malignant stereotypes* (2021).** Considered as a dataset-audit reference; out of scope (closer to `### Datasets and Empirical Grounding` Phase 12).

---

## Editorial decisions taken during curation

- **AI-native + simulation-engine-specific double constraint held cleanly.** The roadmap brief named "algorithmic impact assessment frameworks, distributional harm taxonomies, responsible AI rubrics, governance frameworks". None of those broad categories were curated as standalone entries; instead each curated entry passes both the AI-native test (depends on a learned simulator, RL, generative agents, or AI-augmented method) and the simulation-engine-specific test (addresses a risk that arises *because the artefact is a social-simulation engine*).
- **Boundary with `### Responsible AI` held without entry movement.** No entry moved between sections. Weidinger 2023, Obermeyer 2019, and NIST AI RMF stay in `### Responsible AI` as the canonical generic-AI safety / fairness-case-study / RMF references. `### Ethical Risk Discovery` curated entries each add a *simulation-engine* contribution Weidinger / Obermeyer / NIST do not provide.
- **Group 2 ended at three entries rather than the floor of two.** D'Amour 2020 (canonical *fairness-via-simulation* + open-source ML-fairness-gym artefact), Liu 2018 (canonical *delayed-impact* baseline), and Heidari 2019 (canonical *effort-unfairness* extension) form a three-paper core that an audit of a learned policy should reproduce as a baseline. Multi-Agent Multi-Objective RL for Climate Equity (arXiv 2505.01115) and Creager 2020 *Causal Modeling for Fairness in Dynamical Systems* (ICML 2020) deferred to Phase 15 cross-cutting gaps to avoid lineage saturation.
- **Group 3 held at the floor of two entries.** Stadler 2022 covers synthetic-population leakage (the privacy / dual-use risk every AI-native simulator inherits). Park 2024 covers learned deception transferring out of game / negotiation simulators (the second-order-harm pathway specific to generative-agent simulators). The literature for misuse / dual-use research *specific* to AI-native social simulation is thinner than generic AI-misuse literature; flagged to Phase 15.
- **Group 4 held at the floor of one entry.** Solaiman et al. 2023 is the cross-cutting categorical framework an AI-native simulation engine's risk layer reuses. Mökander 2023 (3-layer LLM audit) and Raji 2020 (end-to-end internal algorithmic auditing) are stronger generic-auditing references but fail the simulation-engine-specific test; deferred to Phase 13 (Tools) consideration.
- **8 entries within the 8–10 target.** At the lower edge of the target range. The thinner candidate pool for *AI-native + simulation-engine-specific* risk discovery is the binding constraint; Group 3 in particular is dominated by either generic AI-misuse research (out of scope) or by the simulators themselves (already curated elsewhere).
- **Flat list, no sub-headings.** All eight entries sit flat under `### Ethical Risk Discovery`. The 18 sections in the Resource Map are fixed.
- **No cross-reference block at section foot.** Mirrors Phase 10 per the *Decisions* block in `requirements.md`. Cross-section entries (Weidinger 2023, Obermeyer 2019, NIST AI RMF, Hermans 2022, Talts 2018, Park 2023 *Generative Agents*, Gao 2025 *AgentSociety*, Yang 2024 *OASIS*, Vezhnevets 2023 *Concordia*) are not duplicated; readers find them through the existing section index.

---

## Open gaps to revisit in Phase 15 (cross-cutting gaps)

- **Distributional-equity-via-MARL on policy simulators.** Multi-Agent Multi-Objective RL for Climate Equity (arXiv 2505.01115) and follow-ups remain the most promising substrate for a Phase 15 entry on equity-objective MARL applied directly to learned policy simulators.
- **Causal fairness in dynamical systems applied to AI-native simulators.** Creager 2020 (ICML) and follow-ups would close the gap between `### Causal Inference` (which holds the Dyer 2024 interventional-surrogates entry) and `### Ethical Risk Discovery` (Group 2 audit methods).
- **False-policy-authority research specific to learned simulators.** No primary reference yet on the failure mode where a policy-maker treats a learned simulator's confident-looking counterfactual as authoritative despite miscalibration. Hermans 2022 (`### Uncertainty Quantification`) is the closest substrate; the *policy-authority* contribution is open.
- **Simulated-society as influence-operations infrastructure.** Burtell & Woodside 2023 is the closest analysis; a research-lab equivalent has not yet surfaced. Re-evaluate after the next NeurIPS-Safety / FAccT cycle.
- **Non-Western risk-discovery perspectives.** All curated entries are Western-research-lab work. The non-Western coverage gap flagged in `mission.md` and `docs/09-policy-and-intervention-modelling.md` extends to Phase 11; flag for Phase 15 with priority on Asian and African research-lab work on AI risk discovery for policy simulators.
- **Long-horizon institutional-drift risk.** No curated entry models how policy authority erodes or institutions adapt under repeated learned-simulation-driven decision-making. Decade-and-longer institutional dynamics under simulation-supported policy is an open area.
- **Interpretability-for-risk-discovery on learned simulators.** Deferred to Phase 13 (Tools and Libraries) where mechanistic-interpretability and probing tools may surface. The `### Ethical Risk Discovery` cut here is risk-surfacing methodology; the tools that implement it sit in Phase 13.
- **Risk-discovery benchmarks.** Welfare Diplomacy (Mukobi et al. 2024) and equivalent cooperative-AI benchmarks deferred to Phase 14 (Benchmarks and Testbeds) where the benchmark framing is the right home.
