# _Robots in Disguise_: Fundamental AI Reading Group

Public repo for The Alan Turing Institute's reading group on fundamental AI research.

If you're based at the Turing, follow `#robots-in-disguise` on the Turing Slack for the most recent updates.

**To see all the slides and reading materials for previous sessions, see the [archive](PREVIOUS.md).**

Note that this originated from the [Research Engineering Team](https://www.turing.ac.uk/research-engineering)'s reading group on Transformers.

## Overview

The group meets every <b>week on Mondays at 11-12</b>. Everyone is welcome to join! If you have any questions email [Ryan Chan](mailto:rchan@turing.ac.uk), [Fede Nanni](mailto:fnanni@turing.ac.uk) or [Giulia Occhini](go292@cam.ac.uk) and remember to go through our [Code of Conduct](CodeOfConduct.md) before joining.

Please **get in touch** if you would like to give a talk (either about your research or a topic you think is relevant to the reading group) add suggestions and emoji preferences to the [list of proposed topics](https://hackmd.io/4zHl_1G6Se-yumHTN48dqg?both) on HackMD!

## Upcoming Schedule

|Date | Topic | Room | Lead |
| --- | ----- | ---- | ---- |
| [07/10/24](#071024) | Invited Talk: Federating Large Language Models from Scratch | David Blackwell | [Lorenzo Sani](https://www.cst.cam.ac.uk/people/ls985) |
| [14/10/24](#141024) | Invited Talk: Causal Estimation of Memorisation Profiles | David Blackwell | [Pietro Lesci](https://pietrolesci.github.io/) |
| [16/10/24](#161024) | Mechanistic Interpretability III | Jack Good | [Ryan Chan](https://github.com/rchan26) |
| [21/10/24](#211024) | Invited Talk: Building new multilingual evals and synthetic post training techniques for low resource languages | David Blackwell | [Ed Bayes](https://www.linkedin.com/in/edbayes/) |
| [28/10/24](#281024) | No Language Left Behind (NLLB) Technical Report Overview | David Blackwell | [Giulia Occhini](https://github.com/giuliaok), [Ryan Chan](https://github.com/rchan26) |
| [04/11/24](#041124) | Invited Talk: Ethnographic Approaches to AI Evaluations | Ursula Franklin | [Jonas Kgomo](https://www.equiano.institute/people/jonas) |
| [11/11/24](#111124) | Scaling laws of neural networks | David Blackwell | [Edmund Dable-Heath](https://github.com/eddableheath) |
| [18/11/24](#181124) | Application of foundation models in time series tasks | David Blackwell | [Gholamali Aminian](https://www.turing.ac.uk/people/researchers/gholamali-aminian) |
| [25/11/24](#251124) | TBC | David Blackwell | TBC |
| [02/12/24](#021224) | TBC | David Blackwell | TBC |
| [09/12/24](#091224) | TBC | David Blackwell | TBC |
| [16/12/24](#161224) | TBC | David Blackwell | TBC |


# Material for sessions

## 07/10/24
### Federating Large Language Models from Scratch

Large language models (LLMs) offer unprecedented ML capabilities and continue to improve rapidly. As a result, various organizations are locked in a race to scale LLMs and explore their limits and weaknesses. We believe federated learning (FL) offers an untapped potential to dramatically increase the supply of data sources for these models. Early work has shown, for example, how LLM pre-training can tap into edge device data leveraging FL. Others have shown the impact of using federated optimizers in a poorly connected distributed infrastructure of stateful workers to train a centralized LLM.

We believe FL can reshape LLM practices and opportunities thanks to two of its most exciting features: relaxed synchronization requirements and privacy-by-design on users' data. The federated paradigm opens the doors of new interesting possibilities for the LLM community, like resource sharing, unbounded scaling on private data, democratization, and privacy. This talk contributes to the emerging field that blends the two worlds of FL and LLMs by presenting a fully federated approach for LLM pre-training from scratch. Our approach has shown to be viable at a scale of 3B parameters under a real working system.

- [The Future of Large Language Model Pre-training is Federated](https://arxiv.org/pdf/2405.10853)

## 16/10/24
### Mechanistic Interpretability III
- [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/)
- [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/)
- [Scaling and evaluating sparse autoencoders](https://arxiv.org/abs/2309.08600)
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://arxiv.org/abs/2309.08600)

## 28/10/24
### No Language Left Behind (NLLB)

- [No Language Left Behind: Scaling Human-Centered Machine Translation (Report)](https://research.facebook.com/publications/no-language-left-behind/)
- [Scaling neural machine translation to 200 languages (Nature paper)](https://www.nature.com/articles/s41586-024-07335-x)
- [No Language Left Behind (NLLB) project](https://ai.meta.com/research/no-language-left-behind/)
