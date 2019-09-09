## Q
What is **Ordinary Least Squares** regression?

## A
**Ordinary Least Squares** is one scoring method to fit a linear regression. In OLS, we estimate the parameters/coefficients that minimize the squared distance between each point in our dataset and our predicted values.

OLS requires that multiplying our observation data matrix by its transpose will result in an intervible matrix.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;
\begin{align}
y = X \beta + \epsilon \\
y = X \beta \\
X^{T}y =  X^{T}X \beta \\
(X^{T}X)^{-1}X^{T}y =  (X^{T}X)^{-1}X^{T}X \beta \\
(X^{T}X)^{-1}X^{T}y = \hat{\beta}
\end{align}
" class="mx-auto d-block" style="background-color:white;"/>

## Q
What is the interpretation of the **R^2** metric? When is it useful?

## A
**R^2** is a statistical measure of how close the data are fit to our regression line. **R^2** is interpretted as the percentage of the dependent variable that is explained by the model. For this reason the **R^2** is also known as the **coefficient of determination**. We won't go into the calculation of $R^2$ today, just know that a higher $R^2$ percentage is nearly always better and indicates a model that fits the data more closely.

In predictive modeling, we care more about minimizing Root-Mean-Squared-Error than maximizing **R^2**. If we add any feature to our model (even nearly meaningless ones) **R^2** will improve. For this reason, while higher **R^2** generally means a better model, it's not what we're trying to optimize.

## Q
What is **Polynomial Regression**?

## A

## Q
What is **Log-Linear Regression**?

## A

## Q
What are **Interaction Terms**?

## A
**Interaction Terms** are features that increase model performance which are created as a function of 2 or more other features in our observed data. Most commonly **Interaction Terms** are made by multiplying other features together.

Some predictive models (like trees) can explore feature interactions automatically. However, in OLS regression, we must define these interaction terms explicitly.

## Q
What is **Multi-Collinearity**? Why is it a problem for OLS regression?

## A
**Multi-Collinearity** means that two columns are linearly dependant on or related to each other. This is problematic for OLS because the determinant of the X matrix will be zero, causing it to not be invertible. This will greatly harm models that are calculated using the linear algebra approach to Ordinary Least Squares regression.

A common "trap" is using one-hot-encoding on a binary variable, which produces two columns that are perfect opposites of each other.

## Q
How does OLS handle outliers?

## A
OLS coefficients are strongly biased by outliers. They should be handled before modeling.

## Question
What is a **Variance Inflation Factor**?

## Answer
The variance inflation factor (or VIF for short), is the ratio of variance in a model with multiple terms, divided by the variance of a model with one term alone. It quantifies the severity of multicollineartiy in an ordinary least squares regression analysis. It provides an index that measures how much the variance(the square of the estimate's standard deviation) of an estimated regression coefficient is increased because of collinearity.

## q
What is **Regularization** intuitively? What are the 2 main types? (other flashcards ask about specifics)

## a
**Regularization** increases model bias and thus reducing variance (overfitting the model to the noise in the data). Regularization "waters down" coefficients with a penalty typically based on some sort of distance metric.

The 2 main types are **L1 Regularization** and **L2 Regularization**.

## q
What is **L1 Regularization**?

## a
**L1 Regularization**, or **Lasso Regression**, reduces unimportant coefficients to zero.

## q
What is **L2 Regularization**?

## a
**L2 Regularization**, or **Ridge Regression**,is ordinary least squares regression with a loss function that minimizes the **sum of square error of residuals** and **the squared slope of the fit model `* alpha`**.

The `alpha` parameter corresponds to the weight being given to the extra penalty being calculated by [Tikhonov regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization) (this parameter is also referred to as &lambda;	in the context of ridge regression).

Ridge regression with `alpha=0` is the same as vanilla linear regression. As `alpha` increases, we give more penalty to a steep slope. In effect, we penalize coefficient size. Each coefficient represents the slope of an individual dimension (feature) of the model, so ridge regression is just squaring and summing those.

As `alpha` approaches infinity, the penalty gets so extreme that coefficients converge to 0 (any non-zero coefficient would outweigh any improvement in the residuals), and just fit a flat model with intercept at the mean of the dependent variable.

In ridge regression, **scaling the data helps**. Then our cost is consistent and can be added uniformly across features, and it is simpler to search for the `alpha` parameter.
