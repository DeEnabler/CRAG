# Corrective Retrieval Augmented Generation
This repository releases the source code for the paper:
- [Corrective Retrieval Augmented Generation](https://arxiv.org/pdf/2401.15884.pdf). <br>
  Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling <br>

## Overview
Large language models (LLMs) inevitably exhibit hallucinations since the accuracy of generated texts cannot be secured solely by the parametric knowledge they encapsulate. Although retrieval-augmented generation (RAG) is a practicable complement to LLMs, it relies heavily on the relevance of retrieved documents, raising concerns about how the model behaves if retrieval goes wrong. To this end, we propose the **Corrective Retrieval Augmented Generation (CRAG)** to improve the robustness of generation. Specifically, a lightweight retrieval evaluator is designed to assess the overall quality of retrieved documents for a query, returning a confidence degree based on which different knowledge retrieval actions can be triggered. Since retrieval from static and limited corpora can only return sub-optimal documents, large-scale web searches are utilized as an extension for augmenting the retrieval results. Besides, a decompose-then-recompose algorithm is designed for retrieved documents to selectively focus on key information and filter out irrelevant information in them. CRAG is plug-and-play and can be seamlessly coupled with various RAG-based approaches. Experiments on four datasets covering short- and long-form generation tasks show that CRAG can significantly improve the performance of RAG-based approaches.

<div align=center>
  <img src="https://github.com/DeEnabler/CRAG/blob/main/img/img-crag.PNG" width=80%>
</div>


## Requirements
**Note: We use Python 3.11 for CRAG** To get started, install conda and run:
```
git clone https://github.com/deenabler/CRAG.git
conda create -n CRAG python=3.11
...
pip install -r requirements.txt
```

## Cite
If you think our work is helpful or use the code, please cite the following paper:

```
@article{yan2024corrective,
  title={Corrective Retrieval Augmented Generation},
  author={Yan, Shi-Qi and Gu, Jia-Chen and Zhu, Yun and Ling, Zhen-Hua},
  journal={arXiv preprint arXiv:2401.15884},
  year={2024}
}
```
