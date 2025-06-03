# LOGIC Dataset

This task was originally framed as a classification task. For the purposes of this research, we adapted it to follow an MCQ (multiple-choice question) format, where the `context` is the fallacy statement, and each of the fallacy types is listed as answer `options`.

For example

```
Statement: Everyone knows that teenagers are lazy

Question: Which type of logical fallacy is this an example of?

Options

A. Faulty generalisation
B. False causality
C. Circular claim
D. Appeal to emotion
E. Deductive fallacy
F. False dilemma
G. Fallacy of credibility

```

# Distribution of instances

| Logical Fallacy | Base set | Ann set |
| ------------- | ----|----|
| Faulty generalisation | 289 | 17 |
| False causality | 154 | 15 |
| Circular claim | 112 | 15 |
| Appeal to emotion | 109 | 15 |
| Deductive fallacy | 120 | 15 |
| False dilemma | 118 | 17 |
| Fallacy of credibility | 95 | 16 |
| Total | 1000 | 110 |

For detailed information on how the instances were selected to create the *base* and *annotation* sets, refer to section `B.2 Fallacy detection` in the paper's appendix.
