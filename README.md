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
| [23/09/24](#230924) | Mechanistic Interpretability | Ursula Franklin | [Ryan Chan](https://github.com/rchan26) |
| [30/09/24](#300924) | Mechanistic Interpretability | David Blackwell | [Ryan Chan](https://github.com/rchan26) |
| [07/10/24](#071024) | Invited Talk: Federating Large Language Models from Scratch | David Blackwell | [Lorenzo Sani](https://www.cst.cam.ac.uk/people/ls985) |
| [14/10/24](#141024) | Invited Talk: Causal Estimation of Memorisation Profiles | David Blackwell | [Pietro Lesci](https://pietrolesci.github.io/) |
| [21/10/24](#211024) | Invited Talk: Building new multilingual evals and synthetic post training techniques for low resource languages | David Blackwell | TBC |
| [28/10/24](#281024) | No Language Left Behind (NLLB) Technical Report Overview | David Blackwell | [Giulia Occhini](https://github.com/giuliaok), [Ryan Chan](https://github.com/rchan26) |
| [04/11/24](#041124) | TBC | David Blackwell | TBC |
| [11/11/24](#111124) | TBC | David Blackwell | TBC |
| [18/11/24](#181124) | Application of foundation models in time series tasks | David Blackwell | [Gholamali Aminian](https://www.turing.ac.uk/people/researchers/gholamali-aminian) |
| [25/11/24](#251124) | TBC | David Blackwell | TBC |
| [02/12/24](#021224) | TBC | David Blackwell | TBC |
| [09/12/24](#091224) | TBC | David Blackwell | TBC |
| [16/12/24](#161224) | TBC | David Blackwell | TBC |


# Material for sessions

## 23/09/24
### Mechanistic Interpretability I
- [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)
- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/)
- [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/)
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717)

## 30/09/24
### Mechanistic Interpretability II
- [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/)
- [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/news/mapping-mind-language-model)
- [Scaling and evaluating sparse autoencoders](https://arxiv.org/abs/2309.08600)
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://arxiv.org/abs/2309.08600)

## 07/10/24
### Federating Large Language Models from Scratch

Large language models (LLMs) offer unprecedented ML capabilities and continue to improve rapidly. As a result, various organizations are locked in a race to scale LLMs and explore their limits and weaknesses. We believe federated learning (FL) offers an untapped potential to dramatically increase the supply of data sources for these models. Early work has shown, for example, how LLM pre-training can tap into edge device data leveraging FL. Others have shown the impact of using federated optimizers in a poorly connected distributed infrastructure of stateful workers to train a centralized LLM.

We believe FL can reshape LLM practices and opportunities thanks to two of its most exciting features: relaxed synchronization requirements and privacy-by-design on users' data. The federated paradigm opens the doors of new interesting possibilities for the LLM community, like resource sharing, unbounded scaling on private data, democratization, and privacy. This talk contributes to the emerging field that blends the two worlds of FL and LLMs by presenting a fully federated approach for LLM pre-training from scratch. Our approach has shown to be viable at a scale of 3B parameters under a real working system.

- [The Future of Large Language Model Pre-training is Federated](https://arxiv.org/pdf/2405.10853)

## 28/10/24
### No Language Left Behind (NLLB)

- [No Language Left Behind: Scaling Human-Centered Machine Translation (Report)](https://research.facebook.com/publications/no-language-left-behind/)
- [Scaling neural machine translation to 200 languages (Nature paper)](https://www.nature.com/articles/s41586-024-07335-x)
- [No Language Left Behind (NLLB) project](https://ai.meta.com/research/no-language-left-behind/)
