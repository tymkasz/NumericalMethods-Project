# Comparative Analysis of Random Number Generators (TRNG vs. PRNG) in Monte Carlo Simulations

A project analyzing the impact of Random Number Generator (RNG) quality on the accuracy and stability of numerical simulations. The study compares a **True Random Number Generator (TRNG)** based on quantum phenomena with standard **Pseudo-Random Number Generators (PRNG)**.

## Project Overview

The primary objective of this project is to verify whether the source of randomness affects the convergence of Monte Carlo methods. The main case study involves estimating the value of $\pi$ using the geometric method.

The research demonstrates that the determinism of simple algorithms (like LCG) can lead to significant systematic errors and geometric anomalies (the Marsaglia effect), which often remain undetected by basic statistical tests.

## Analyzed Generators

1.  **ANU Quantum Random Numbers (TRNG)**
    * **Type:** Hardware Entropy Source.
    * **Source:** Quantum vacuum fluctuations (Australian National University).
    * **Role:** Offers true randomness.

2.  **Mersenne Twister (MT19937)**
    * **Type:** PRNG (Pseudo-Random Number Generator).
    * **Usage:** The default generator in Python, C++, and Excel.
    * **Features:** Massive period ($2^{19937}-1$) and high statistical quality.

3.  **Linear Congruential Generator (LCG)**
    * **Type:** Simple PRNG ($X_{n+1} = (aX_n + c) \mod m$).
    * **Parameters:** $m=2^{32}$, $a=1664525$, $c=1013904223$ (per *Numerical Recipes*).
    * **Role:** Demonstration of structural flaws and linear correlations.

## Methodology

The project utilizes three main analytical tools:

1.  **Monte Carlo Simulation ($\pi$ Estimation)**
    * Analysis of absolute error as a function of sample size ($N$).
    * Verification of stochastic convergence against the theoretical model $\sigma \approx 1.64/\sqrt{N}$.
    * Detection of structural defects (lattice structure).

2.  **Chi-Square Goodness of Fit Test ($\chi^2$)**
    * Testing for uniformity of distribution.
    * Verifying the null hypothesis (p-value analysis).

3.  **Shannon Entropy**
    * Measurement of information density and bit sequence disorder.

## Key Results and Findings

### 1. Stability vs. Chaos
* **ANU Quantum:** Exhibited ideal stochastic convergence consistent with statistical theory. The error decreases proportionally to $1/\sqrt{N}$.
* **Mersenne Twister:** Proved to be a highly stable engineering alternative to TRNG, effectively emulating random processes without observable bias.

### 2. The Downfall of LCG and Seed Sensitivity
The study revealed critical flaws in the LCG algorithm:
* **Seed=32:** Unnaturally fast convergence caused by points fitting deterministically into the circle's geometry.
* **Seed=87:** Total lack of convergence (persistent high error).
* **Seed=123345678:** Showed cyclic resonance—regular, sharp drops in error occurring approximately every 75k samples.

### 3. The "Blind Test" Paradox
It was proven that the LCG algorithm can pass the **Chi-Square Test** with excellent results (producing a perfectly flat histogram) while simultaneously failing the **Monte Carlo Test** completely (exhibiting fatal geometric correlations).
> **Conclusion:** Frequency tests are a necessary but insufficient condition for assessing the cryptographic safety of a generator.

## Tech Stack

* **Python 3.13.2**
* `matplotlib` - Data visualization (logarithmic scale).
* `numpy` - Numerical computations.
* `scipy` - Statistical tests (Chi-square, Entropy).
* `requests` - Fetching live data from the ANU Quantum API.

## License

This project is licensed under the MIT License. Quantum data is sourced from the Australian National University (ANU) Quantum Random Numbers Server.
