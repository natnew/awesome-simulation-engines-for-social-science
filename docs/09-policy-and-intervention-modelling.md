# Phase 10 — Policy and Intervention Modelling: Research Notes

**Status:** Private — local only, never to be pushed or made public
**Date:** 2026-05-10

These notes record candidate research and editorial decisions that did not survive the cut into the canonical `### Policy and Intervention Modelling` section of `README.md`. The README is authoritative; this file is only supplementary research context for future review passes (Phase 15 cross-cutting gaps and Phase 16 reference-architecture update).

---

## Methodology vs domain map

| Curated entry | Domain | Methodology | Source |
|---|---|---|---|
| Capobianco et al. 2021 (JAIR) | Public health / epidemic | RL over agent-based community simulator | Sony AI + UT Austin + Texas A&M |
| Chopra et al. 2023 (Vaccine) | Public health / epidemic (vaccine policy) | Neural-network calibration of differentiable ABM | MIT Media Lab + Mayo Clinic HEAL + Georgia Tech + Michigan |
| Du et al. 2023 (Information Sciences, HRL4EC) | Public health / epidemic (multi-mode NPI) | Hierarchical RL over MID-SEIR | Jilin University + NTU + Dalian University of Technology |
| Wu et al. 2022 (IEEE T-RO, Flow) | Urban / transport / mobility | Deep RL framework wrapping SUMO | UC Berkeley |
| Wei et al. 2018 (KDD, IntelliLight) | Urban / transport / mobility (traffic signals) | Deep Q-learning over real traffic data | Penn State |
| Strnad et al. 2019 (Chaos) | Climate-economy / IAM | Deep RL over coupled World-Earth model | PIK Potsdam |
| Zhang et al. 2022 / ICML 2025 (RICE-N) | Climate-economy / IAM | MARL with negotiation protocols over multi-region IAM | Mila + Salesforce Research |
| Dütting et al. 2024 (JACM) | Cross-domain methodology | Differentiable mechanism design / auctions | Google Research + Harvard EconCS |

---

## Candidates considered but not curated

### Public health / epidemic

- **Kompella et al. 2020 *Reinforcement Learning for Optimization of COVID-19 Mitigation Policies* (arXiv:2010.10560).** Same Sony AI / UT Austin group as the curated Capobianco et al. JAIR 2021 entry. The JAIR paper is the peer-reviewed extended version, so the arXiv preprint is dropped to avoid lineage duplication.
- **Hierarchical-RL for resource-constrained NPI cluster control (arXiv:2603.19397, March 2026).** Recent and methodologically interesting (hierarchical RL with restless multi-armed bandit framing for resource allocation across clusters), but not yet peer-reviewed. Re-evaluate at Phase 15 when the venue settles.
- **HRL4EC (Du et al. 2023) was retained for the non-Western coverage.** The decision was between Du et al. (Jilin University) and the Liang et al. neural-traffic / urban-policy line; the public-health framing won because the public-health area carried the higher floor (≥2 entries) and the non-Western mission gap is most visible in epidemic policy where Asian and African research-lab work is systematically under-cited in Western-trained models.
- **EpidemiOptim (Colas et al. 2021).** RL toolbox for epidemic-control policy optimisation. Considered for inclusion; deferred because the canonical reference is more methodology-survey than deployed-simulator artefact and the underlying epidemic model is a stylised SEIR rather than a community-scale ABM. Re-evaluate if a follow-up applies it to a larger simulator.
- **AgentTorch *On the Limits of Agency in Agent-Based Models* (Chopra et al., AAMAS 2025)** is already in `### Agent-Based Modelling` as the methodological entry. The curated Vaccine 2023 paper is the *applied* counterpart, not a duplicate.

### Urban / transport / mobility

- **Vinitsky, Lichtlé, Parvate & Bayen — *Optimizing Mixed Autonomy Traffic Flow with Decentralized Autonomous Vehicles and Multi-Agent Reinforcement Learning* (ACM TCPS 2023).** Strong candidate; the decentralised-MARL extension of the Flow framework. Not curated to keep Group 2 at two entries and avoid double-counting the Berkeley line. If the section is later expanded to ten or more entries, this is the next obvious add.
- **CityFlow (Zhang et al., WWW 2019).** The simulator that several signal-control RL papers were retargeted to after IntelliLight. Not curated because IntelliLight is the primary methodological reference and CityFlow is more of a tooling artefact; a `### Tools and Libraries` cross-reference is the right home for it in Phase 13.
- **Chu, Wang, Codecà & Li — *Multi-agent deep reinforcement learning for large-scale traffic signal control* (MA2C, IEEE TITS 2020).** Cooperative MARL over CityFlow / SUMO. Strong candidate; not curated to avoid Group 2 lineage saturation.
- **TrafficSim (Suo et al., CVPR 2021)** is already in `### Machine-Learned World Models` and not duplicated here.

### Climate-economy / IAM

- **Rolnick et al. — *Tackling Climate Change with Machine Learning* (ACM Comp Surv 2022, arXiv:1906.05433).** A landscape paper, not a deployed policy simulator; out of scope per the *Not entries* clause in `requirements.md`. Re-curate consideration deferred to Phase 13 (Tools and Libraries) or Phase 15 (cross-cutting gaps) if a survey reference is wanted somewhere.
- **Climate Surrogates for Scalable MARL (CICERO-SCM case study, arXiv 2510.07971).** A 2025 follow-up to the RICE-N work using neural-surrogate climate models inside MARL. Not curated because the Strnad and RICE-N entries already cover the "RL on climate-economy" methodology and CICERO-SCM follow-up is methodologically incremental. Re-evaluate if it appears at a peer-reviewed venue with broader uptake.
- **Multi-Agent Multi-Objective RL for Climate Equity (arXiv 2505.01115).** Methodology paper extending RICE-N with multi-objective rewards for distributional fairness. Strong candidate for Phase 15 cross-cutting gaps (distributional analysis); not curated here to keep Group 3 focused on canonical primary references.

### Cross-domain methodology

- **AI Economist (Zheng et al., Science Advances 2022)** is already in `### Agent-Based Modelling`. RICE-N (curated Group 3) is the climate-policy follow-up from the same Salesforce / Stanford line; the original AI Economist taxation paper is not duplicated here.
- **Dyer, Bishop, Felekis, Zennaro, Calinescu, Damoulas & Wooldridge — *Interventionally Consistent Surrogates for Complex Simulation Models* (NeurIPS 2024)** is already in `### Causal Inference` and not duplicated.
- **LLM-mediated policy sandboxes** (Park et al. follow-ups, AgentSociety policy-experiment papers). Considered; not curated because the strongest candidates (Park et al. *Generative Agents*, Gao et al. *AgentSociety*) are already in `### Social Simulation` / `### LLM-Based Social Simulation`, and the policy-specific follow-ups have not yet matured into a clean primary reference.
- **Mechanism-design RL** beyond Dütting et al. — e.g., Curry et al. revenue-maximising auctions with differentiable economics (AISTATS 2022); Tang & Sandholm contract design via deep learning. Not curated to avoid lineage saturation in mechanism-design / auction work; Dütting et al. is the JACM 2024 canonical reference.

---

## Editorial decisions taken during curation

- **AI-native pivot held cleanly.** The roadmap brief named UKMOD, EUROMOD, Covasim, OpenABM-Covid19, EURACE, MATSim. None were curated. The Sony AI PandemicSimulator (Capobianco et al.) is the AI-native counterpart to Covasim / OpenABM-Covid19 in the curated list; Flow (Wu et al.) is the AI-native counterpart to MATSim; RICE-N (Zhang et al.) is the AI-native counterpart to EURACE / DICE / RICE.
- **Three required domains, fiscal / tax dropped.** Confirmed at bootstrap. AI Economist (already in `### Agent-Based Modelling`) covers the AI-native fiscal-policy slot. Dütting et al. (curated Group 4) covers the broader mechanism-design methodology that subsumes optimal-tax-design as a special case.
- **8 entries within the 8–10 target.** Lower than Phase 9's 12. The thinner candidate pool for AI-native applied policy is the binding constraint; the canonical-lineage Group 1 / Group 2 / Group 3 / Group 4 references that survive the AI-native + research-lab + stable-reference + non-duplicate gate sit at roughly 8 entries, with another 4–5 plausible second-line entries listed under *Candidates considered* above.
- **Flat list, no sub-headings.** All eight entries sit flat under `### Policy and Intervention Modelling`. The 18 sections in the Resource Map are fixed.
- **No cross-reference block at section foot.** Diverges from Phase 9 per the *Decisions* block in `requirements.md`. Cross-section entries (AI Economist, AgentTorch, TrafficSim, CitySEIRCast, Andrianakis 2015) are listed under *Candidates considered* above with the section they live in noted, so the editorial trace is preserved without bloating the README.

---

## Open gaps to revisit in Phase 15 (cross-cutting gaps)

- **Distributional / equity analysis of policy outcomes.** Curated entries optimise for aggregate ICU load, system-level traffic flow, or cooperative climate outcomes; they do not surface distributional harm by demographic group. The Multi-Agent Multi-Objective RL for Climate Equity (arXiv 2505.01115) line is the most promising substrate for this gap.
- **Long-run temporal dynamics.** Most curated entries operate on weeks-to-years horizons. Decade-and-longer policy dynamics (institutional drift, intergenerational climate effects) are under-represented in the AI-native policy literature; flag for Phase 15 review.
- **Trust, legitimacy, and governance simulation.** No curated entry directly models how citizens accept or resist policy, or how legitimacy erodes under repeated intervention. LLM-mediated policy sandboxes are the closest substrate but were deferred in this phase.
- **Compounding and cascading risk.** Curated entries treat policy domains in isolation (epidemic OR traffic OR climate-economy). Multi-domain cascade modelling (e.g., epidemic policy → labour-market shock → mobility change → secondary infection) is not represented here and is a clear Phase 15 / Phase 16 follow-up.
- **AI-native fiscal-policy beyond AI Economist.** AI Economist is in `### Agent-Based Modelling`; the canonical second-generation AI-native fiscal-policy paper has not yet emerged. Worth a review pass after the next NBER / NeurIPS-Economics-of-AI cycle.
