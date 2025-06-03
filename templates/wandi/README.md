# Write and Improve (WandI) Essay Scoring Dataset

The W&I corpus contains submissions (defined as *essays*) that have been manually annotated with a coarse Common European Framework of Reference for Languages (CEFR) level by trained raters. 
Levels correspond to language proficiency levels ranging from A1 (elementary) to C2 (complete proficiency) from a second-language learner’s perspective.

This task was originally framed as a classification task. For the purposes of this research, we adapted it to follow an MCQ (multiple-choice question) format, where the `context` is the essay, and each of the CEFR levels is listed as answer `options`.

For example

```
Essay:
To: International organisation
From: Dimitris Barberis
Subject: Our green town

Introduction
The aim of the report is to write how are town take care of the environment. I do a research and this are findings.

Rubbish
We have a lot of bins around the area, so now we can throw our litters whenever we are. Also we have recycle bins for paper and glass.

Cleaners
Every Saturday our local cleaning team clean the park and now everyone can ejoy it!

Conclusion
We do everything to make our town more green, our citizens always have new ideas that make the difference of our daily life.

Question: If you were to assign a grade to this essay, what would it be?

Options:

A. Beginner (grade A)
B. Intermediate (grade B)
C. Advanced (grade C)

```

# Distribution of instances

| Essay Grade | Base Set | Ann set |
| ------------- | ----|----|
| A | 333 | 36 |
| B | 334 | 37 |
| C | 333 | 37 |
| Total | 1000 | 110 |

For detailed information on how the instances were selected to create the *base* and *annotation* sets, refer to section `B.4 Essay Scoring` in the paper's appendix.
