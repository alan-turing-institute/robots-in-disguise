# Transformers Reading Group

Public repo for the [Research Engineering Team](https://www.turing.ac.uk/research-engineering)'s reading group on Transformers.

Follow `#hut23-robots-in-disguise` on Slack for the most recent updates.

## Overview

The group meets every <b>2 weeks on Mondays at 11am</b>. Everyone is welcome to join! If you have any questions email [Ryan](mailto:rchan@turing.ac.uk).

The plan is to learn about transformer models (assuming little knowledge of deep learning and NLP) with the end goal of implementing a transformers model from scratch.

Please add suggestions and emoji preferences to the [list of proposed topics](https://hackmd.io/NILcoBk1QquVNkDR6dbIBA) on HackMD.

## Schedule

|Date | Topic | Room | Lead |
| --- | ----- | ---- | ---- |
| 20/03/23 | Introduction to word embeddings and language modelling ([Slides](https://docs.google.com/presentation/d/1i56HKtjcdQFTxacxsjgya_giDx8Mv1xZn-IDNc_mK8I/edit?usp=sharing)) | David Blackwell | [Fede Nanni](https://github.com/fedenanni) |
| 03/04/23 | Deep Learning Basics ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/02-deep-learning/Robots_Neural_Networks_2023-04-03.pptx)) | David Blackwell | [Phil Swatton](https://github.com/philswatton) & [Jack Roberts](https://github.com/jack89roberts) |
| 17/04/23 | Sequence-to-sequence models part I: RNNs/LSTMs ([Slides](https://github.com/alan-turing-institute/transformers-reading-group/blob/main/sessions/03-seq2seq-part-i/seq2seq_part1_hut23_robots_in_disguise.pdf)) | David Blackwell | [Ryan Chan](https://github.com/rchan26) |
| 01/05/23 | Sequence-to-sequence models part II: Encoder-decoder models | David Blackwell | [Ryan Chan](https://github.com/rchan26) |
| 15/05/23 | Hands-on RNN/LSTM session | David Blackwell | N/A |
| 29/05/23 | Attention and self-attention networks | David Blackwell | [Martin Stoffel](https://github.com/mastoffel) |
| 12/06/23 | Hack Week | David Blackwell | N/A |
| 26/06/23 | Transformer Encoder and Decoders | David Blackwell | N/A |
| 10/07/23 | Tokenizers, Masked Language modelling and Pre-training | David Blackwell | N/A |
| 24/07/23 | Huggingface tutorial | David Blackwell | N/A |

# Material for sessions

## Introduction to Word Embeddings and Language modelling

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
    
## Deep Learning Basics

**Main**
- [Neural Networks and Deep Learning | Chapter 1: Using neural nets to recognize handwritten digits](http://neuralnetworksanddeeplearning.com/chap1.html)
- [Neural Networks and Deep Learning | Chapter 2: How the backpropagation algorithm works](http://neuralnetworksanddeeplearning.com/chap2.html)
  - Alternatively, come along to [Phil and Jack's Lunchtime Tech Talk](https://github.com/alan-turing-institute/DataScienceSkills/wiki/Lunchtime-Tech-Talks) on Back Propagation (April 11th) - message on the `#hut23-robots-in-disguise` slack if you want to get a calendar invite for the session

**Extra**
- [Learning Deep Learning | Chapters 1 and 2](https://jack89roberts.github.io/learning-deep-learning/index.html)
- [Neural Networks by Hand | Feedforward Neural Networks](https://philswatton.github.io/neural-networks-by-hand/feedforward-neural-network.html)
- [Andrej Karparthy (YouTube): The spelled-out intro to neural networks and backpropagation](https://youtu.be/VMj-3S1tku0)

## Sequence-to-sequence models part I: RNNs/LSTMs

**Main**
- [Speech and Language Processing | Chapter 9: RNNs and LSTMs](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
  - Read up to Section 9.5 (read pages 1-13)

**Extra**
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [NLP with Deep Learning Stanford Course | Lecture 5](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf)
  - Read up to Section 3 (read pages 1-11)
- [Stanford NLP with Deep Learning | Lecture 5: RNNs)](https://you.be/PLryWeHPcBs)

## Sequence-to-sequence models part II: Encoder-decoder models

**Main**
- [Speech and Language Processing | Chapter 9: RNNs and LSTMs](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
  - Read from 9.5 to 9.8 (read pages 14-21)
  
**Extra**
- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [NLP with Deep Learning Stanford Course | Lecture 5](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf)
  - Read from Section 3 (read pages 11 onwards)
- [Stanford NLP with Deep Learning | Lecture 6: Simple LSTM RNNs](https://youtu.be/0LixFSa7yts)

---

**Note**: material below is not confirmed for the session yet...
  
**Attention**
- [Michigan Deep Learning for Comp Vis | Lecture 13: Attention](https://www.youtube.com/watch?v=YAgjfMR9R_M)
- [Speech and Language Processing | Chapter 9: RNNs and LSTMs](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
  - Read from 9.8 (read pages from 21 onwards)
- [Speech and Language Processing | Chapter 10: Transformers and Pretrained Language Models](https://web.stanford.edu/~jurafsky/slp3/10.pdf)
- [NLP with Deep Learning Stanford Course | Lecture 6](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes06-NMT_seq2seq_attention.pdf)
- [Stanford NLP with Deep Learning | Lecture 7: Translation, Seq2Seq, Attention](https://youtu.be/wzfWHP6SXxY)
- [Attention and Augmented Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/)
