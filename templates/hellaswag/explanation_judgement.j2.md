# Explanation Judging Task

Your task is to evaluate a set of explanations in a given context. We define the context (**Task**, **Audience**, and **Purpose**) in the following way:

**Task**: you will be shown a series of multiple-choice questions relating to one of four tasks (commonsense reasoning, fallacy detection, reading comprehension and essay scoring) in the following format:
1. **Question**: The question being answered.
2. **Answer Choices**: The possible answer choices for that question.
3. **Correct Answer**: The correct answer to the question.
4. **User Answer**: The answer provided by the user.
5. **Explanation**: The explanation provided by the user to support their answer.

**Audience**: you should assume that the audience of the explanations is adult, English-proficient, and provided in a formal academic setting.

**Purpose**: the explanations should provide an understanding of why a certain answer was chosen for a given multiple-choice question.

---

## Evaluation Criteria

For the given explanation, please answer the following questions with either **Yes** or **No**. Note that you **should not consider the correctness of the user's answer** when evaluating the explanation. Focus solely on the quality of the explanation according to the criteria provided.

1. **Action**: Does the explanation clearly indicate the decision or choice being made (e.g., specifying the selected answer)?
    - Answer **Yes** if it does. For example "The correct answer is A."
    - Answer **No** if it does not. For example "Because it is the final part of the sequence."

2. **Reason**: Does the explanation provide reasoning or insight into why the decision or choice was made, explaining the underlying logic or rationale for the **Action**?
    - Answer **Yes** if it does. For example "The right answer is C because it is the final part of the sequence."
    - Answer **No** if it does not. For example "The correct answer is A."

3. **Grammaticality**: Is the explanation grammatically correct and free of lexical or syntax errors? Small typos are acceptable, but the errors should not impede comprehension in any way.
    - Answer **Yes** if it is. For example "The correct answer is A because nowadays our society is based on consumerism and the way in which we are producing is contaminating the world."
    - Answer **No** if it is not. For example "The correct answer is A because now a day our socity it is bassed in consumer, so that become the word more contaminate to produce the products that we demanding."

4. **Word Choice**: Is the language used in the explanation tailored to the given context (task, audience, purpose)? And are the sentences in the explanation well-formed?
    - Answer **Yes** if they are. For example "The correct answer is A because the essay lacks fluency. There are many incorrect clauses and missing words. And while the overall meaning can be deduced, the essay does not demonstrate an accurate grasp of language (e.g., frequent spelling and punctuation errors)."
    - Answer **No** if they are not. For example "Answer A. lack of fluency, incorrect clauses and missing words, meaning can be found but does not demonstrate an accurate grasp of language"

5. **Cohesion**: Does the explanation make appropriate use of transition phrases (e.g., connectives like "because", "therefore", "consequently", overlapping words across sentences, etc.)?
    - Answer **Yes** if it does. For example "The correct answer is C because the man is on roller blades, not on a skateboard. Further, he is not talking to anyone and therefore cannot possibly 'continue speaking.'"
    - Answer **No** if it does not. For example "The correct answer is C, because the man is on roller blades, not a skateboard, and is not talking to anyone in the example so cannot 'continue speaking'".

6. **Conciseness**: Is the explanation free of any redundant, irrelevant, or excess sentences (that is, not required to understand the answer)?
    - Answer **Yes** if it is. For example "The correct answer is D because it accurately reflects the sequence of events."
    - Answer **No** if it is not. For example, given that the option D was "next she explains how to use the lawnmower and other tools and then she cuts the grass", the following explanation is not concise: "The correct answer is D because the sentence mentions that she explains how to use the lawnmower and other tools, and then she cuts the grass. Option D accurately reflects the sequence of events."

7. **Appropriateness**: Is the explanation culturally appropriate, matching expectations for the given context?
    - Answer **Yes** if it is. For example "The right answer is B because the tenses are properly used and the story makes sense."
    - Answer **No** if it is not. For example "The right answer is B because the tenses are properly used and (within the slightly odd context) the story makes sense."

8. **Coherence**: Does the explanation appropriately transition between ideas? That is, does the explanation make sense as a whole (e.g., good context-relatedness, semantic consistency, and inter-sentence causal and temporal dependencies, etc.)?
    - Answer **Yes** if it does. For example "The correct answer is D, because no information about Liu's relationship to science subjects specifically is given in the passage, therefore the fact that they like chemistry is implied and ambiguous."
    - Answer **No** if it does not. For example "The correct answer is D, because no information about Liu's relationship to science subjects specifically is given in the passage, therefore the fact that they like cheese is implied and ambiguous."

9. **Evidence**: Does the explanation provide concrete evidence (can be both explicit or implicit) that supports the reasoning, such as information from the question's context or general knowledge?
    - Answer **Yes** if it does. For example "The right answer is C, because it finishes the sequence, describing the effect of bowling the ball and what happens as a result."
    - Answer **No** if it does not. For example "The right answer is C, because is is the final part of the sequence."

10. **Plausibility (of the evidence)**: Is the provided evidence plausible and consistent with human reasoning, considering the context and general world knowledge?
    - Answer **Yes** if it is. For example "The correct answer is A ('Jack picks the cheese') because we are told that he enjoys eating 'mozzarella' in the morning."
    - Answer **No** if it is not. For example "The correct answer is A ('Jack picks the cheese') because my name is also Jack and I personally love cheese for breakfast."

11. **Affective Appeals**: Does the explanation use vivid, or emotionally charged language (e.g., metaphors) to evoke feelings in the audience?
    - Answer **Yes** if it does. For example "The expression in the final section is very heartfelt; the tone is excitable and keen throughout."
    - Answer **No** if it does not. For example "The final section reflects the writer's strong feelings on this issue."

12. **Qualifiers**: Does the explanation make use of hedges, boosters, attitude markers, self-mentions, or engagement markers to clarify the writer's stance (i.e., the explainer's personal feelings towards the task)? Note that the stance can be implicit unlike the **Action**.
    - Answer **Yes** if it does. For example "The right answer is B, because the text is keeping with what is presumably a tour guide's voice: intentionally using clunky and overly expressive words."
    - Answer **No** if it does not. For example "The right answer is B, because the text is keeping with the original tour guide's voice."

13. **Stance Clarity**: Is the explainer's stance (their personal feelings towards the task) clearly and unambiguously conveyed through affective appeals or qualifiers? Note that the stance can be implicit unlike the Action.
    - Answer **Yes** if it is. For example "The correct answer is A (beginner) because this text is undeniably of a low English level."
    - Answer **No** if it is not. For example "The correct answer is A (beginner) because this text is clearly of a low English level although the final section is incredibly well written."

---

## Expected Output

Your answers should be formatted as follows:

1. Action: **Yes** or **No**
2. Reason: **Yes** or **No**
3. Grammaticality: **Yes** or **No**
4. Word Choice: **Yes** or **No**
5. Cohesion: **Yes** or **No**
6. Conciseness: **Yes** or **No**
7. Appropriateness: **Yes** or **No**
8. Coherence: **Yes** or **No**
9. Evidence: **Yes** or **No**
10. Plausibility: **Yes** or **No**
11. Affective Appeals: **Yes** or **No**
12. Qualifiers: **Yes** or **No**
13. Stance Clarity: **Yes** or **No**

---

## Question
{{ctx_a | trim}}

## Answer Choices
A. {{ctx_b}} {{endings[0] | trim}}
B. {{ctx_b}} {{endings[1] | trim}}
C. {{ctx_b}} {{endings[2] | trim}}
D. {{ctx_b}} {{endings[3] | trim}}

## Correct Answer
{{correct_answer | trim}}

## User Answer
{{user_answer | trim}}

## Explanation
{{explanation | trim}}
