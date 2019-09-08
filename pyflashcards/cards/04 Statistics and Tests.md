## q
What is the difference between **parametric statistics** and **nonparametric statistics**? What are some examples?

## a
**Parametric statistics** [(wiki)](https://en.wikipedia.org/wiki/Parametric_statistics) assumes certain things about the population we are studying and allows us to model probabilities with a fixed set of paramters. For example, a normal distribution has two parameters: the mean and the standard deviation.

Typically parametric methods are applied in cases where the population is approximately normal or can be approximated using a normal distribution via the **central limit theorem**. 

Common parametric assumptions:

* confidence interval for a population mean, with known standard deviation
* confidence interval for a population mean, with unknown standard deviation
* confidence interval for a population variance
* confidence interval for the difference of two means, with unknown standard deviation

Parametric methods:

* **t-test**
* Pearson correlation test
* most well known statistical methods

**Nonparametric statistics** [(wiki)](https://en.wikipedia.org/wiki/Nonparametric_statistics) is not based solely on parametrized families of probability distributions (parameters like mean and variance). Nonparametric statistics is based on either being distribution-free or having a specified distribution but with the distribution's parameters unspecified. Nonparametric statistics includes both descriptive statistics and statistical inference.

Nonparametric models/methods:

* A histogram is a simple nonparametric estimate of a probability distribution (and Kernel density estimation)
* K Nearest Neighbors classify the unseen instance based on the K points in the training set which are nearest to it
* chi-squared test
* Bootstrapping techniques
* Spearman correlation test

## q
What is **Standard Deviation**? How do we compute it for a sample with an assumed normal-distributed population? What is its unit of measure?

## a
**Standard Deviation**, &sigma;, is a measure of how spread out our measurements are. Specifically, it is the average distance from the mean, in the same units as our unit of measure.

<img src="../static/img/standard_deviation.svg" style="background-color:white;"/>

```python
def mean(arr):
  return sum(a_list) / len(arr)

def standard_deviation(arr, bessels=True):
  arr_mean = mean(arr)
  n = len(a_list) - bessels
  variance = sum([(i - arr_mean) ** 2 for i in arr]) / n
  return  variance ** 0.5
```

---

## q
What is **Variance**? How do we compute it for a sample with an assumed normal-distributed population? How do we compute it from the **Standard Deviation**?

## a

**Variance**, &sigma;^2, is a measure of how spread out our measurements are. **Variance** is the average of the squared differences from the mean.

```python
def mean(arr):
  return sum(a_list)/len(arr)

def variance(arr, bessels=True):
  arr_mean = mean(arr)
  n = len(a_list) - bessels
  return sum([(i - arr_mean) ** 2 for i in arr]) / n

# OR

def standard_deviation(arr, bessels=True):
  arr_mean = mean(arr)
  n = len(a_list) - bessels
  variance = sum([(i - arr_mean) ** 2 for i in arr]) / n
  return  variance ** 0.5

def variance(arr, bessels=True):
  return standard_deviation(arr, bessels) ** 2
```

---

## Q
When considering **Variance** and **Standard Deviation**, why might we use one over the other?

## A
**Standard Deviation** can be understood as the square root of **Variance**. Mathematically, the square root puts the measurement back in the same units as our unit of measure.

---

## Q
What is **Covariance**? What is a **Variance-Covariance Matrix**?

## A
**Covariance** is a measure of how changes in one variable are associated with changes in a second variable.

A large positive or negative covariance indicates a strong relationship between two variables. However, we can't necessarily compare covariances between pairs of variables that have a different scale. Since covariance values are unbounded, they could take on arbitrarily high or low values. A variable that has a large scale will always have a higher covariance than a variable with an equally strong relationship, yet smaller scale. This means that we need to **regularlize** (i.e. use correlation coefficient), which removes the unit understanding from the measures.

<img src="../static/img/stats_covariance.svg" class="mx-auto d-block" style="background-color:white;"/>

A **Variance-Covariance Matrix** is a square matrix that compares each variable with every other variable in a dataset and returns the variance values along the main diagonal and covariance values everywhere else.

```python
import pandas as pd

df = pd.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
                  columns=['dogs', 'cats'])
df.cov()
```

```
>>>           dogs      cats
    dogs  0.063333 -0.056667
    cats -0.056667  0.070000
```

---

## Q
What is a **Correlation Coefficient**? How does this compare to **Covariance**?

## A

The measure of spread of a variable is the Standard Deviation. If we divide our covariance values by the product of the standard deviations of the two variables, we'll end up with what's called the (Pearson) **Correlation Coefficient**, *r*.

Correlation coefficients have a fixed range from -1 to +1 with, 0 representing no linear relationship between the data.

In most use cases the correlation coefficient is an improvement over measures of covariance because:
* Covariance can take on practically any number while a correlation is limited: -1 to +1.
* Because of it’s numerical limitations, correlation is more useful for determining how strong the relationship is between the two variables.
* Correlation does not have units. Covariance always has units
* Correlation isn’t affected by changes in the center (i.e. mean) or scale of the variables

<img src="../static/img/stats_corr.svg" class="mx-auto d-block" style="background-color:white;"/>

```python
import pandas as pd

df = pd.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
                  columns=['dogs', 'cats'])
df.corr()
```

```
>>>           dogs      cats
    dogs  1.000000 -0.851064
    cats -0.851064  1.000000
```

---

## q
At what "degrees of freedom" parameter is a **t-Distribution** considered normal for reseach purposes?

## a
30

## q
What is **Inferential Statistics**?

## a
**Inferential statistics** generalizes from a sample to a broader population with a calculated degree of certainty.
