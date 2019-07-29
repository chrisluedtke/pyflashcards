##### Question
What is a **Variance Inflation Factor**?

##### Answer
The variance inflation factor (or VIF for short), is the ratio of variance in a model with multiple terms, divided by the variance of a model with one term alone. It quantifies the severity of multicollineartiy in an ordinary least squares regression analysis. It provides an index that measures how much the variance(the square of the estimate's standard deviation) of an estimated regression coefficient is increased because of collinearity.

##### Tags
linear models, machine learning, regression

----

## q
What is **Regularization** intuitively? What are the 2 main types? (other flashcards ask about specifics)

## a
**Regularization** increases model bias and thus reducing variance (overfitting the model to the noise in the data). Regularization "waters down" coefficients with a penalty typically based on some sort of distance metric.

The 2 main types are **L1 Regularization** and **L2 Regularization**.

## q
What is **L1 Regularization**?

## a
**L1 Regularization**, also known as **Lasso Regression** reduces unimportant coefficients to zero.

## q
What is **L2 Regularization**?

## a
**L2 Regularization**, also known as **Ridge Regression** is ordinary least squares regression with a loss function that minimizes the **sum of square error of residuals** and **the squared slope of the fit model `* alpha`**.

The `alpha` parameter corresponds to the weight being given to the extra penalty being calculated by [Tikhonov regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization) (this parameter is also referred to as $\lambda$ &lambda;	&#955; in the context of ridge regression).

Ridge regression with `alpha=0` is the same as vanilla linear regression. As `alpha` increases, we give more penalty to a steep slope. In effect, we penalize coefficient size. Each coefficient represents the slope of an individual dimension (feature) of the model, so ridge regression is just squaring and summing those.

As `alpha` approaches infinity, the penalty gets so extreme that coefficients converge to 0 (any non-zero coefficient would outweigh any improvement in the residuals), and just fit a flat model with intercept at the mean of the dependent variable.

In ridge regression, scaling the data helps. Then our cost is consistent and can be added uniformly across features, and it is simpler to search for the `alpha` parameter.