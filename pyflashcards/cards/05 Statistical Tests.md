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
How do we compute the **standard deviation** of a sample, with an assumed normal-distributed population?

## a
<img src="/static/img/standard_deviation.svg">

## q
How do we compute the **variance** of a sample from its **standard deviation**, with an assumed normal-distributed population?

## a
```python
variance = standard_deviation ** 2
```

## q
At what "degrees of freedom" parameter is a **t-distribution** considered normal for reseach purposes?

## a
30

## q
What is **inferential statistics**?

## a
**Inferential statistics** generalizes from a sample to a broader population with a calculated degree of certainty.