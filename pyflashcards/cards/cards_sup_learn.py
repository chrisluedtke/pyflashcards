cards_sup_learn = """\
QUESTION
What is a confusion matrix?

ANSWER
A contingency table (AKA cross tabulation), where rows and columns
represent the predicted class and the actual class.

TAGS
supervised learning, classification, validation, unit 2
-------------------------
QUESTION
What are true positives, false positives, true negatives, and
false negatives?

ANSWER
 true positives: predicted positive and actually positive
false positives: predicted positive and actually negative
 true negatives: predicted negative and actually negative
false negatives: predicted negative and actually positive

TAGS
supervised learning, classification, validation, unit 2
-------------------------
QUESTION
What is RECALL in classification models?

ANSWER
N true positives / N actual positives
 ~OR~
N true positives / (N true positives + N false negatives)
 ~OR~
The percent of actual positives that we correctly
labeled as positive.

TAGS
supervised learning, classification, validation, unit 2
-------------------------
QUESTION
What is PRECISION in classification models?

ANSWER
N true positives / (N true positives + N false positives)
 ~OR~
N true positives / N predicted positives
 ~OR~
The percent of our positive predictions that were actually
positive.

TAGS
supervised learning, classification, validation, unit 2
-------------------------
QUESTION
What do we import to run logistic regression in sklearn?

ANSWER
>>> from sklearn.linear_model import LogisticRegression

TAGS
supervised learning, classification, validation, unit 2
"""
