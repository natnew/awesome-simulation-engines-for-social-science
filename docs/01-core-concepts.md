# Core Concepts

Building a learned social simulation engine requires a shared understanding of several key architectural and methodological concepts.

## 1. Bounded System Slices

A **Bounded System Slice** is a modular, self-contained model of a specific social domain.
- **Boundaries:** Clearly defined limits on what is included and excluded.
- **Inputs & Outputs:** Standardised interfaces for data and signal flow.
- **Perturbations:** Specific points where interventions or external shocks can be applied.
- **Composability:** The ability for separate slices to interact via defined APIs.

## 2. Learned Simulators (World Models)

Unlike traditional rule-based simulators, a **Learned Simulator** (or world model) learns system dynamics from data.
- **Data-Driven:** Trained on historical, observational, and synthetic data.
- **Latent Dynamics:** Identifies hidden patterns and causal structures that are not explicitly programmed.
- **Stochasticity:** Represents uncertainty and variability as probability landscapes rather than single-point forecasts.

## 3. Synthetic Populations

A **Synthetic Population** is a demographically and behaviourally realistic representation of individuals and entities within a simulation.
- **Realism:** Matches the statistical distributions of real-world populations.
- **Granularity:** Allows for micro-level analysis of distributional effects.
- **Privacy-Preserving:** Provides a way to model social systems without using sensitive personal data.

## 4. Counterfactual Experimentation

**Counterfactual Experimentation** is the process of testing "what-if" scenarios by intervening in the simulation.
- **Intervention Modelling:** Applying changes to policies, incentives, or environmental conditions.
- **Path Exploration:** Simulating multiple plausible futures under the same intervention.
- **Comparison:** Measuring the difference between the intervened state and a baseline (control) state.

## 5. Emergence and Feedback

Social systems are characterised by **Emergence**—where micro-level actions produce macro-level outcomes—and **Feedback Loops**, where system states influence future behaviour.
- **Non-Linearity:** Small changes can lead to disproportionately large effects.
- **Adaptation:** Agents change their behaviour in response to interventions or environmental shifts.

## 6. Uncertainty Quantification (UQ)

**Uncertainty Quantification** is the practice of measuring and communicating the limits of what the simulation can predict.
- **Calibration:** Ensuring the simulation's probability distributions align with real-world evidence.
- **Sensitivity Analysis:** Identifying which assumptions or inputs have the greatest impact on the outcome.
- **Probability Landscapes:** Presenting results as a range of possible outcomes with associated likelihoods.

## How this applies to this repository

These concepts form the **evaluation criteria** for the resources we include. We prioritise tools that treat uncertainty as a first-class citizen, frameworks that enable modular composability, and datasets that support high-fidelity synthetic populations. By understanding these concepts, contributors can better identify resources that fit the "Learned Social Simulation Engine" mission.
