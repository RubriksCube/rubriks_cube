# Rubrik's Cube

[![Static Badge](https://img.shields.io/badge/arXiv-2503.23899-b31b1b?logo=arXiv)](https://arxiv.org/abs/2503.23899)
[![Static Badge](https://img.shields.io/badge/Main-ACL_2025-red)](https://aclanthology.org/2025.acl-long.1160/)
![GitHub Repo stars](https://img.shields.io/github/stars/RubriksCube/rubriks_cube?style=flat&logo=GitHub)
![GitHub last commit](https://img.shields.io/github/last-commit/RubriksCube/rubriks_cube?path=README.md&style=flat&logo=GitHub)


Repo for the paper "[Rubrik's Cube: Testing a New Rubric for Evaluating Explanations on the CUBE dataset](https://aclanthology.org/2025.acl-long.1160/)" (ACL 2025) by Diana Galvan-Sosa*, Gabrielle  Gaudeau*, Pride Kavumba, Yunmeng Li, Hongyi gu, Zheng Yuan, Keisuke Sakaguchi, Paula Buttery

# News
- **[2025.07.23]**  We added the explanations and evaluations for the `annotation` and `evaluation` sets to `data/`
- **[2025.06.05]**  We updated the camera-ready version on [arXiv](https://arxiv.org/abs/2503.23899) 
- **[2025.05.15]**  Our paper is accepted at [ACL 2025](https://2025.aclweb.org/program/main_papers/) Main! See you in Vienna ~


# What this repo contains
## Data
- The CUBE dataset, in `data/` 

Currently, the directory contains explanations and evaluations for two of the three subsets (`annotation set` and `evaluation set`) described in the paper. We'll update it with the remaining subset soon.

## Code
- *Add description*

# Citation
```bibtex
@inproceedings{galvan-sosa-etal-2025-rubriks,
    title = "Rubrik{'}s Cube: Testing a New Rubric for Evaluating Explanations on the {CUBE} dataset",
    author = "Galvan-Sosa, Diana  and
      Gaudeau, Gabrielle  and
      Kavumba, Pride  and
      Li, Yunmeng  and
      Gu, Hongyi  and
      Yuan, Zheng  and
      Sakaguchi, Keisuke  and
      Buttery, Paula",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.1160/",
    pages = "23800--23839",
    ISBN = "979-8-89176-251-0",
    abstract = "The performance and usability of Large-Language Models (LLMs) are driving their use in explanation generation tasks. However, despite their widespread adoption, LLM explanations have been found to be unreliable, making it difficult for users to distinguish good from bad explanations. To address this issue, we present Rubrik{'}s CUBE{--}an education-inspired rubric and a dataset of 26k explanations, written and later quality-annotated using the rubric by both humans and six open- and closed-source LLMs. The CUBE dataset focuses on two reasoning and two language tasks, providing the necessary diversity for us to effectively test our proposed rubric. Using Rubrik, we find that explanations are influenced by both task and perceived difficulty. Low quality stems primarily from a lack of conciseness in LLM-generated explanations, rather than cohesion and word choice. The full dataset, rubric, and code are available at https://github.com/RubriksCube/rubriks{\_}cube."
}
```

# Contact
- For future collaboration requests, feel free to email Diana Galvan-Sosa and Gabrielle Gaudeau.
- For coding-related questions, please use GitHub Issues. Feel free to tag Pride Kavumba and Hongyi gu.
- For dataset collection-related questions, please use GitHub Issues. Feel free to tag Diana Galvan-Sosa.
