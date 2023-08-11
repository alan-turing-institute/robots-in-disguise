# Transformers Reading Group

Public repo for the [Research Engineering Team](https://www.turing.ac.uk/research-engineering)'s reading group on Transformers.

Follow `#hut23-robots-in-disguise` on Slack for the most recent updates.

## Overview

The group meets every <b>2 weeks on Mondays at 11-12</b>. Everyone is welcome to join! If you have any questions email [Ryan](mailto:rchan@turing.ac.uk).

The plan is to learn about transformer models (assuming little knowledge of deep learning and NLP) with the end goal of implementing a transformers model from scratch.

Please add suggestions and emoji preferences to the [list of proposed topics](https://hackmd.io/4zHl_1G6Se-yumHTN48dqg?both) on HackMD.

## Schedule

|Date | Topic | Room | Lead |
| --- | ----- | ---- | ---- |
| [20/03/23](#200323) | Introduction to word embeddings and language modelling ([Slides](https://docs.google.com/presentation/d/1i56HKtjcdQFTxacxsjgya_giDx8Mv1xZn-IDNc_mK8I/edit?usp=sharing)) | David Blackwell | [Fede Nanni](https://github.com/fedenanni) |
| [03/04/23](#030423) | Deep Learning Basics ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/02-deep-learning/Robots_Neural_Networks_2023-04-03.pptx)) | David Blackwell | [Phil Swatton](https://github.com/philswatton), [Jack Roberts](https://github.com/jack89roberts) |
| [17/04/23](#170423) | Sequence-to-sequence models part I: RNNs/LSTMs ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/03-seq2seq-part-i/seq2seq_part1_hut23_robots_in_disguise.pdf)) | David Blackwell | [Ryan Chan](https://github.com/rchan26) |
| [03/05/23](#030523) | Sequence-to-sequence models part II: Encoder-decoder models ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/04-seq2seq-part-ii/seq2seq_part2_hut23_robots_in_disguise.pdf)) | David Blackwell | [Ryan Chan](https://github.com/rchan26) |
| 15/05/23 | Hands-on RNN/LSTM session ([Materials](https://github.com/phinate/jax-rnn))| David Blackwell | [Nathan Simpson](https://github.com/phinate), [Levan Bokeria](https://github.com/lbokeria), [David Llewellyn-Jones](https://github.com/llewelld) |
| [31/05/23](#310523) | Reginald overview & Attention and self-attention networks ([Notebook](https://github.com/alan-turing-institute/transformers-reading-group/tree/main/REGinalds/gpt2-demo)) | David Blackwell | [Evelina Gabasova](https://github.com/evelinag), [Martin Stoffel](https://github.com/mastoffel) |
| [26/06/23](#260623) | Attention (continued) ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/05-attention/attention.pdf)) & Transformer Encoder and Decoders ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/06-transformers-architecture/transformer_architecture_hut23_robots_in_disguise.pdf)) | David Blackwell | [Martin Stoffel](https://github.com/mastoffel), [Ryan Chan](https://github.com/rchan26) |
| [10/07/23](#100723) | BERT: Masked Language modelling and Pre-training ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/07-bert/bert_hut23_robots_in_disguise.pdf)) | David Blackwell | [Ryan Chan](https://github.com/rchan26) |
| [24/07/23](#240723) | GPT: Pretraining Decoders ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/08-gpt/gpt_hut23_robots_in_disguise.pdf)) | David Blackwell | [Ryan Chan](https://github.com/rchan26) |
| [07/08/23](#070823) | Vision Transformers part I | David Blackwell | [Katie Awty-Carroll](https://github.com/klh5), [Ryan Chan](https://github.com/rchan26) |
| [21/08/23](#210823) | Vision Transformers part II | David Blackwell | [Katie Awty-Carroll](https://github.com/klh5) |
| 04/09/23 | **No session due to RSECon23** | David Blackwell | N/A |
| [18/09/23](#180923) | LoRA (+ parameter efficient fine-tuning) | David Blackwell | [Jack Roberts](https://github.com/jack89roberts) |
| [02/10/23](#021023) | Reinforcement Learning Human Feedback (RLHF) | David Blackwell | [Eseoghene Ben-Iwhiwhu](https://github.com/dlpbc) |
| [16/10/23](#161023) | Prompt Engineering | David Blackwell | [Martin Stoffel](https://github.com/mastoffel) |
| [30/10/23](#301023) | Introduction to Diffusion models | David Blackwell | Edmund Dable-Heath |
| [13/11/23](#131123) | Stable Diffusion | David Blackwell | Edmund Dable-Heath |
| 27/11/23 | N/A | David Blackwell | N/A |
| 11/12/23 | N/A | David Blackwell | N/A |

# Material for sessions

## 20/03/23
### Introduction to Word Embeddings and Language modelling

**Main**
  - [Don't Count, Predict! paper](https://aclanthology.org/P14-1023.pdf)
  - [Word Embeddings (1)](https://www.ruder.io/word-embeddings-1/)
  - [Word Embeddings (2)](https://www.ruder.io/word-embeddings-softmax/)
  - [Word Embeddings (3)](https://www.ruder.io/secret-word2vec/)
  - [Brief History of NLP (part 1)](https://medium.com/@antoine.louis/a-brief-history-of-natural-language-processing-part-1-ffbcb937ebce)
  - [Brief History of NLP (part 2)](https://medium.com/@antoine.louis/a-brief-history-of-natural-language-processing-part-2-f5e575e8e37)

**Extra**
  - [Deep Learning, NLP and Representations](http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/)
  - [Stanford NLP with Deep Learning | Lecture 1: Intro & Word Vectors](https://youtu.be/rmVRLeJRkl4)
  - [Speech and Language Processing - Chapter 6: Vector Semantics and Embeddings](https://web.stanford.edu/~jurafsky/slp3/6.pdf)
  - [Stanford Large Language Models | Lecture 1: Introduction](https://stanford-cs324.github.io/winter2022/lectures/introduction/)
    
## 03/04/23
### Deep Learning Basics

**Main**
- [Neural Networks and Deep Learning | Chapter 1: Using neural nets to recognize handwritten digits](http://neuralnetworksanddeeplearning.com/chap1.html)
- [Neural Networks and Deep Learning | Chapter 2: How the backpropagation algorithm works](http://neuralnetworksanddeeplearning.com/chap2.html)
  - Alternatively, come along to [Phil and Jack's Lunchtime Tech Talk](https://github.com/alan-turing-institute/DataScienceSkills/wiki/Lunchtime-Tech-Talks) on Back Propagation (April 11th) - message on the `#hut23-robots-in-disguise` slack if you want to get a calendar invite for the session

**Extra**
- [Learning Deep Learning | Chapters 1 and 2](https://jack89roberts.github.io/learning-deep-learning/index.html)
- [Neural Networks by Hand | Feedforward Neural Networks](https://philswatton.github.io/neural-networks-by-hand/feedforward-neural-network.html)
- [Andrej Karparthy (YouTube): The spelled-out intro to neural networks and backpropagation](https://youtu.be/VMj-3S1tku0)

## 17/04/23
### Sequence-to-sequence models part I: RNNs/LSTMs

**Main**
- [Speech and Language Processing | Chapter 9: RNNs and LSTMs](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
  - Read up to Section 9.5 (read pages 1-13)

**Extra**
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [NLP with Deep Learning Stanford Course | Lecture 5](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf)
  - Read up to Section 3 (read pages 1-11)
- [Stanford NLP with Deep Learning | Lecture 5: RNNs)](https://you.be/PLryWeHPcBs)

## 03/05/23
### Sequence-to-sequence models part II: Encoder-decoder models

**Main**
- [Speech and Language Processing | Chapter 9: RNNs and LSTMs](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
  - Read from 9.5 to 9.8 (read pages 14-21)
  
**Extra**
- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [NLP with Deep Learning Stanford Course | Lecture 5](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf)
  - Read from Section 3 (read pages 11 onwards)
- [Stanford NLP with Deep Learning | Lecture 6: Simple LSTM RNNs](https://youtu.be/0LixFSa7yts)

## 31/05/23
### Attention

**Main**
- [Attention is all you need](https://arxiv.org/abs/1706.03762)

**Extra**
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Andrej Karpathy's GPT-2 from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=4766s)
- [Anthropic's Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)
- [NLP with Deep Learning Stanford Course | Lecture 6](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes06-NMT_seq2seq_attention.pdf)
- [Attention and Augmented Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/)
- [Stanford NLP with Deep Learning | Lecture 7: Translation, Seq2Seq, Attention](https://youtu.be/wzfWHP6SXxY)
- [Stanford NLP with Deep Learning | Lecture 9: Self- Attention and Transformers](https://youtu.be/ptuGllU5SQQ)
- [Michigan Deep Learning for Comp Vis | Lecture 13: Attention](https://www.youtube.com/watch?v=YAgjfMR9R_M)

## 26/06/23
### Transformer Encoder and Decoders

**Main**
- [Attention is all you need](https://arxiv.org/abs/1706.03762)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/)

**Extra**
- [Speech and Language Processing | Chapter 9: RNNs and LSTMs](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
  - Read from 9.8 (read pages from 21 onwards)
- [Speech and Language Processing | Chapter 10: Transformers and Pretrained Language Models](https://web.stanford.edu/~jurafsky/slp3/10.pdf)
- [NLP with Deep Learning Stanford Course | Self-Attention & Transformers](https://web.stanford.edu/class/cs224n/readings/cs224n-self-attention-transformers-2023_draft.pdf)

## 10/07/23
### BERT: Masked Language modelling and Pre-training

**Main**
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)

**Extra**
- [Speech and Language Processing | Chapter 11: Fine-Tuning and Masked Language Models](https://web.stanford.edu/~jurafsky/slp3/11.pdf)
- [The Illustrated BERT](http://jalammar.github.io/illustrated-bert/)
- [BERT 101 🤗 State Of The Art NLP Model Explained](https://huggingface.co/blog/bert-101)
- [Paper summary — BERT](https://medium.com/analytics-vidhya/paper-summary-bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding-861456fed1f9)

## 24/07/23
### GPT: Pretraining Decoders

**Main**
- [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)

**Extra**
- [Paper summary - Improving Language Understanding by Generative Pre-Training](https://sh-tsang.medium.com/review-gpt-improving-language-understanding-by-generative-pre-training-28f30d39cd10)
- [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

**Note** the below materials for other sessions, or are not confirmed

## 07/08/23
### Vision Transformers part I

**Main**
- [Gradient Based Learning Applied to Document Recognition](https://ieeexplore.ieee.org/document/726791)
- [An Image Is Worth 16x16 Words: Transformers for Image Recongition at scale](https://arxiv.org/pdf/2010.11929.pdf)

**Extra**
- [Vision Transformer for Image Classification - Shusen Wang (YouTube)](https://youtu.be/HZ4j_U3FC94)
- [Neocognitron: A Self-organizing Neural Network Model
for a Mechanism of Pattern Recognition
Unaffected by Shift in Position](https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf)
- [But what is a convolution? - 3Blue1Brown (YouTube)](https://www.youtube.com/watch?v=KuXjwB4LzSA&t=705s)
- [CNN Explainer](https://poloclub.github.io/cnn-explainer/)

## 21/08/23
### Vision Transformers part II

**Main**

**Extra**


## 18/09/23
### LoRA (+ parameter efficient fine-tuning)

## 02/10/23
### Reinforcement Learning Human Feedback (RLHF)

## 16/10/23
### Prompt Engineering

## 30/10/23
### Introduction to Diffusion models

## 13/11/23
### Stable Diffusion

### Tokenizers and Huggingface tutorial

**Main**
- [Huggingface Tokenizer tutorial](https://huggingface.co/learn/nlp-course/chapter2/4?fw=pt)
- [Huggingface `transformers` course](https://huggingface.co/learn/nlp-course/chapter2/1?fw=pt)
