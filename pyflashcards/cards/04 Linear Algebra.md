## Q
What is a **scalar**?

## A
A **scalar** is a single number that is positive, negative, 0 or any other real number.

```python
scalar = 1
scalar = -10.5
```

---

## Q
What is a **vector**?

## A
A **vector** of dimension *n* is an **ordered** collection of *n* elements, which are called **components** (components of vectors are *not* referred to as "scalars")

```python
vect = [2, 4.6, -1, 9]

import numpy as np
vect = np.array([2, 4.6, -1, 9])
```

---

## Q
What is the **norm** of a vector?

## A
The **norm** or **magnitude** of a vector is nothing more than its **length**. Since a vector is just a line (essentially), we can think of it as the hypotenuse of a triangle and use the pythagorean theorem to find the norm of the vector. We're essentially generalizing the equation for the hypotenuse of a triangle to n dimensional space:

<img src="/static/img/vect_norm.PNG" class="mx-auto d-block">

```python
def vector_norm(vector: List):
    return (sum([vector[i]**2 for i in range(len(vector))])**.5)
```

---

## q
What is a **matrix**? What are its **dimensions**?

## a
A **matrix** is a rectangular grid of numbers arranged in rows and columns. The **dimensions** of the matrix are its number of rows and columns (in that order).

These matrices are 2X4.

```python
vect = [[2, 4.6, -1, 9],
        [5,   1,  0, 2]]

import numpy as np
vect = np.array([[2, 4.6, -1, 9],
                 [5,   1,  0, 2]])
```

---

## q
How do we conduct **matrix multiplication**? What does it accomplish?

## a
**Matrix multiplication** applies a transformation like shrinkage, expansion, or rotation.

We can multipy two matrices only if the number of columns of the first matrix is equal to the number of rows of the second matrix.

The unused dimensions of the factor matrices tell us what the dimensions of the product matrix will be. A 2X3 matrix multiplied by a 3X2 matrix will produce a 2X2 matrix.

There is no commutative property of matrix multiplication (we can't switch the order of the matrices and always get the same result).

Matrix multiplication is best understood in terms of vector dot products. To multiply two matrices together, we can take the dot product of each row of the first matrix and each column of the second matrix. The position of the resulting entries will correspond to the row number and column number of the row and column vector that were used to find that scalar.

<img src="/static/img/matrix_mult.PNG" class="mx-auto d-block">

```python
def matrix_multiply(matrix1, matrix2):
    matrix1_n_cols = len(matrix1[0])
    matrix2_n_rows = len(matrix2)
    assert matrix1_n_cols==matrix2_n_rows, 'Matrix1 Columns != Matrix2 Rows'

    matrix2 = transpose_matrix(matrix2)
    product = [[] for _ in range(len(matrix1))]
  
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            assert (len(matrix1[i]) == len(matrix2[j])), 'Matrices Must Be Rectangular'
            product[i].append(vector_dot_product(matrix1[i],matrix2[j]))
    return product

def vector_dot_product(vector1, vector2):
    assert len(vector1) == len(vector2), 'Expected Vectors of Equal Length'

    return sum([vector1[i]*vector2[i] for i in range(len(vector1))])

def rectangular_matrix(matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return False
    return True

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))
```

---

##### Question
How do you find the **determinant** of a Matrix?

##### Answer
The determinant is a property that all *square* matrices possess, denoted with pipes (i.e. |A|).

Given matrix A:
```
A  = [[a, b]
      [c, d]]
```
The determinant is:
```
|A| = ad - bc
```

---

##### Question
What is **Orthogonality**?

##### Answer
Orthogonality is the property that means 'changing A does not change B'. An example of an orthogonal system would be where we skip to the next song on our playlist, and changing the song does not change the volume.

In programming, orthogonality means that when we execute an instruction, nothing but that instruction happens.

----

##### Question
What is a **Linear Combination**?

##### Answer
In linear algebra, we define the concept of linear combinations in terms of vectors. But, it is actually possible to talk about linear combinations of anything...

(scalar)(something 1 ) + (scalar)(something 2) + (scalar)(something 3)

These 'somethings' could be everyday variables like x, y, z etc. or something more complicated like polynomials. A linear combination is a particular way of combining things (variables, vectors, etc.) using scalar multiplication and addition.

----

##### Question
What is **Collinearity**? Why can it be a problem?

##### Answer
Collineartiy is a condition in which some of the independent variables are highly correlated.

Collinearity tends to inflate the variance of at lesat one estimated regression coefficient.

----

##### Question
What is **Variance**?

##### Answer
The average of the squared differences from the Mean.

----

##### Question
What is standard deviation?

##### Answer
A measure of how spread out numbers are.

----

##### Question
What is **Dimensionality**? Why is it important?

##### Answer
The number of rows and columns a matrix has.

Dataframes can be represented as matrix of size = dataframe.shape, and this is important to note if we are adding new features, concantenating more data, or merging two datasets together.

----

##### Question
What is **Matrix Equality**?

##### Answer
Matrices that have the same dimensions, and their corresponding elements are equal.

----

##### Question
What is **Matrix Multiplication**?

##### Answer
Multiplying any two matrices where the number of columns of the first matrix is equal to the number of rows of the second matrix.

----

##### Question
What are some basic applications of linear algebra in Data Science?

##### Answer
Vectors: Rows, Columns Lists, Arrays
Matrices: Tables, Spreadsheets, DataFrames

Linear Modeling: Linear Regression, Logistic Regression, Gradient Descent, etc.

----

##### Question
What is a **Dot Product**?

##### Answer
Dot products represent the scalar quantity equal to the sum of pair-wise products of components in vectorA and vectorB

----

##### Question
What is **Singular Value Decomposition**?

##### Answer
Factorization of a real or complex matrix. It is the generalization of the eigendecomposition of a given matrix using its constituent elements. These constituent parts help make certain subsequent matrix calculations simpler.

----

##### Question
What is **covariance**?

##### Answer
In probability theory and statistics, covariance is a measure of the joint variability of two random variables. If the greater values of one variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values, (i.e., the variables tend to show similar behavior), the covariance is positive.

----

##### Question
What is **Principal Component Analysis**?

##### Answer
Principal Component Analysis(or PCA for short), is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of linearly uncorrelated variables called principal components.

----
