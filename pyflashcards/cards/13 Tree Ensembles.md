##### Question
How do tree ensembles compare to traditional regression in terms of feature interactions?

##### Answer
Tree ensembles can "pick up" interactions. Regression must have these features explicitly defined.

##### Tags
tree models

---

##### Question
What is **bias** in tree/forest models?

##### Answer
A model's bias is a systematic error. A model with too much bias is wrong in consistent ways. Tree models with high bias are overly simple.

e.g. if we classify NYC vs. SF buildings based on one split on elevation (34 ft), it will consistently mis-classify high-elevation NYC buildings and low-elevation SF buildings.

##### Tags
tree models

---

##### Question
In tree/forest models, what are errors due to **variance**?

##### Answer
High-variance models are **overfit** to the idiosyncrasies of the training data. They tend to be wrong in inconsistent ways. When splits are made from nodes with very little data, the generalizations they make are likely to be incorrect.

Models that overfit are unstable and sensitive to small changes in the training data (thus high variance). They are overly complex.

##### Tags
tree models

---

##### Question
In tree/forest models, what parameter can be tuned to affect **Bias-Variance Tradeoff**?

##### Answer
The minimum-node-size threshold. Larger minimum node sizes will have greater bias error (underfit), while smaller minimum node sizes will have greater variance error (overfit).

##### Tags
tree models

---

##### Question
What are **Partial Dependence Plots**?

##### Answer
Partial dependence plots shows the marginal effect one or two features have on the predicted outcome of a machine learning model. A partial dependence plot can show whether the relationship between the target and a feature is linear, monotonous or more complex. e.g., for linear regression models, partial dependence plots always show linear relationships.

##### Tags
tree models

---