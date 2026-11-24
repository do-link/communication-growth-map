# Communication Growth Map 1.0

**An Open, Cross-Disciplinary Coordinate System for Goal Attainment and Relational Well-Being · `CL-WP-2026-01` · `CC BY 4.0`**

[中文 README](./README.md) · [English README](./README.en.md) · [Web Whitepaper](https://do.link/map/) · [Interactive Lab](https://do.link/lab/) · [Open Spec](https://do.link/spec/)

---

![Spider Chart 1.99x Area Distortion vs Dual-Ring Polar Rose Model](./figures/fig2_spider_bias_vs_rose_map.png)

## Executive Abstract

In an era where generative AI can draft speeches, polish business correspondence, and produce structured analytical reports within seconds, live face-to-face human communication has become more—not less—essential as a key determinant of collaborative effectiveness and long-term relational well-being (Deming, 2017; Waldinger & Schulz, 2023). Yet adult communication research and practice remain constrained by three structural limitations:

1. **Single-perspective fragmentation** across isolated traditions (structural, empathetic, or negotiation-focused approaches);
2. **Decontextualized trait scoring**, despite decades of behavioral evidence showing cross-situational trait correlations rarely exceed `r = 0.30` (Mischel, 1968; Mischel & Shoda, 1995; Reis, 2008);
3. **Systematic metacognitive miscalibration**, where subjective self-evaluations correlate with objective performance at only `r = 0.29` across domains (Zell & Krizan, 2014).

**Communication Growth Map 1.0** is an open, cross-disciplinary public coordinate system grounded in **53 peer-reviewed empirical and foundational theoretical works** across interpersonal communication, social-personality psychology, organizational behavior, psychometrics, and information visualization. Anchored on the dual-axis criterion of **Effectiveness (Goal Attainment) × Appropriateness (Relational Maintenance)** (Spitzberg & Cupach, 1984), it defines a four-layer MECE interaction cycle of **8 Core Directions × 40 Role-Scoped Real-World Situations**:

1. **Clear Expression** (`01–05`) — cognitive load & illusion of transparency `[11–13]`
2. **Empathetic Listening** (`06–10`) — active & episodic listening `[14–16]`
3. **Constructive Request** (`11–15`) — compliance underestimation & advice seeking `[17–18]`
4. **Firm and Warm Boundary** (`16–20`) — curvilinear assertiveness & empowered refusal `[19–21]`
5. **De-escalated Disagreement** (`21–25`) — task vs. relationship conflict `[22–24]`
6. **Reliable Cooperation** (`26–30`) — speech acts & language/action commitments `[25–27]`
7. **Authentic Value Signaling** (`31–35`) — market signaling & professional image `[28–30]`
8. **Relational Rupture Repair** (`36–40`) — rupture-and-repair & effective apologies `[31–33]`

At the geometric and measurement layer, we demonstrate that closed spider/radar charts exhibit a **`1.99×` axis-permutation area distortion** on identical profiles (`4 × 88% + 4 × 20%`) alongside default-midpoint anchoring bias (Munzner, 2014; Tversky & Kahneman, 1974). In response, Map 1.0 specifies a **Dual-Ring Polar Rose Model** with honest whitespace for unobserved nodes, paired with a **Three-Layer Competence Iceberg & Dual-Track Calibration Matrix** (`Subjective ○ × Objective ●`) grounded beneath the surface by malleable **Implicit Relational Beliefs** (Dweck & Leggett, 1988) and continuous **Natural Communication Styles** (Wiggins, 1979).

## Reproduce the `1.99×` Radar Chart Distortion Proof

Zero external dependencies (Python 3 standard library only):

```bash
python3 scripts/reproduce_spider_area_bias.py
```

Or explore the interactive dual radar-vs-rose shuffler and `r = 0.29` calibration plane directly in your browser at [https://do.link/lab/](https://do.link/lab/).

## Repository Contents

- [`whitepaper/communication-growth-map-v1.md`](./whitepaper/communication-growth-map-v1.md) — Complete Chinese whitepaper (5 chapters + 53 verified APA references)
- [`figures/`](./figures/) — High-resolution `2200×1340` plates (`fig1`, `fig2`, `fig3`)
- [`spec/taxonomy-8x40.v1.json`](./spec/taxonomy-8x40.v1.json) — Machine-readable schema for all 8 directions × 40 role-scoped situations
- [`references/references.bib`](./references/references.bib) — Complete 53-entry BibTeX bibliography
- [`scripts/reproduce_spider_area_bias.py`](./scripts/reproduce_spider_area_bias.py) — Exhaustive 70-permutation geometric verification script

## Reference Implementation

A free public reference implementation of Communication Growth Map 1.0 is available at **[https://gvjl.com](https://gvjl.com)** (covering all 8 directions × 40 situations). The software is one engineering realization; the open specification itself remains permanently independent under `CC BY 4.0`.

## Scope & Contributions

Version 1.0 is an open literature-grounded specification and has not yet undergone independent large-scale longitudinal psychometric validation. Critiques, empirical studies, counterexamples, and pull requests are warmly welcome.

## Citation

```bibtex
@misc{zhang2026communicationmap,
  title        = {Communication Growth Map 1.0: An Open, Cross-Disciplinary Coordinate System for Goal Attainment and Relational Well-Being},
  author       = {Zhang, Ling},
  howpublished = {Communication Lab Open Whitepaper (CL-WP-2026-01)},
  year         = {2026},
  month        = {11},
  url          = {https://do.link/map/},
  note         = {Open specification licensed under CC BY 4.0. Repository: https://github.com/do-link/communication-growth-map}
}
```

## License

Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE).
