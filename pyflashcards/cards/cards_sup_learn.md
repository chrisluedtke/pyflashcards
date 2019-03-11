##### Question
What is a confusion matrix?

##### Answer
A contingency table (AKA cross tabulation), where rows and columns
represent the predicted class and the actual class.

##### Tags
supervised learning, classification, validation, unit 2

---

##### Question
What are true positives, false positives, true negatives, and
false negatives?

##### Answer
- _true positives_ -- predicted positive and actually positive
- _false positives_ -- predicted positive and actually negative
- _true negatives_ -- predicted negative and actually negative
- _false negatives_ -- predicted negative and actually positive

##### Tags
supervised learning, classification, validation, unit 2

---

##### Question
What is **Recall** in classification models?

##### Answer
`N true positives / N actual positives`
*OR*
`N true positives / (N true positives + N false negatives)``
*OR*
The percent of actual positives that we correctly
labeled as positive.

##### Tags
supervised learning, classification, validation, unit 2

---

##### Question
What is **Precision** in classification models?

##### Answer
`N true positives / (N true positives + N false positives)`

*OR*

`N true positives / N predicted positives`

*OR*

The percent of our positive predictions that were actually
positive.

##### Tags
supervised learning, classification, validation, unit 2

---

##### Question
What do we import to run logistic regression in sklearn?

##### Answer
```python
>>> from sklearn.linear_model import LogisticRegression
```
##### Tags
supervised learning, classification, validation, unit 2

---
