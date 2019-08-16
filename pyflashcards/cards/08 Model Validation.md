##### Question
What is a **confusion matrix**?

##### Answer
A **contingency table** or **cross tabulation**, where rows and columns
represent the predicted class and the actual class.

##### Tags
supervised learning, classification, validation

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
supervised learning, classification, validation

---

##### Question
What is **Recall** in classification models?

##### Answer
`N true positives / N actual positives`

*OR*

`N true positives / (N true positives + N false negatives)`

*OR*

The percent of actual positives that we correctly
labeled as positive.

##### Tags
supervised learning, classification, validation

---

##### Question
What is **Precision** in classification models?

##### Answer
```
N true positives / (N true positives + N false positives)
```

*OR*

```
N true positives / N predicted positives
```

*OR*

The percent of our positive predictions that were actually
positive.

##### Tags
supervised learning, classification, validation


##### Question
What are **k-fold cross validation** and **n-fold cross validation**?

##### Answer
Rather than split a dataset into train/test or train/validate/test, in cross validation we split the dataset into **k** even parts. We then iterate, such that each part takes a turn as our test set while the other parts are trained on. We can then average across these tests to get a sense of our model's performance.

**n-fold cross validation** simply sets **k** to the number of observations we have. This is **deterministic** (there is no random splitting happening - we test every possibility), but it is computationally expensive. This is also known as **leave-one-out**.

##### Tags
supervised learning, classification, validation

---

##### Question
What is **stratification** in model validation on classification problems?

##### Answer
Ensuring that our train and test sets represent our class/target attribute in the same proportions as in our complete dataset.

##### Tags
supervised learning, classification, validation

---
