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

## Q
What is the **Dot Product** of two vetors? What does it produce?

## A
The dot product of two vectors `a` and `b` produces a scalar quantity that is equal to the sum of pair-wise products of the vectors' components. The dot product is commutative and distributive.

<img src="/static/img/vect_dot.svg" class="mx-auto d-block">

```python
def vector_dot_product(vector1, vector2):
    assert len(vector1) == len(vector2), 'Expected Vectors of Equal Length'

    return sum([vector1[i]*vector2[i] for i in range(len(vector1))])
```

## Q
How do we find the **Cross Product** of two vectors? What does it produce?

## A
The **Cross Product** of two vectors produces a third vector that is perpendicular to the first two vectors. 
It is written with a regular looking multiplication sign like `a X b` but is read as "a cross b".

The cross product can be found by creating a 3X3 matrix from the two vectors and the unit vector and then finding the determinant of the 3x3 matrix.

<img src="/static/img/vect_cross.PNG" class="mx-auto d-block">

----

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

## Q
What is **Matrix Equality**?

## A
Two matrices that have the same dimensions, and their corresponding elements are equal.

----

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
    assert matrix1_n_cols == matrix2_n_rows, 'Matrix1 Columns != Matrix2 Rows'

    matrix2 = transpose_matrix(matrix2)  # makes it easier to find cols by index
    product = []
  
    for i, matrix1_row in enumerate(matrix1):
        product.append([])
        for j, matrix2_col in enumerate(matrix2):
            product[i].append(vector_dot_product(matrix1_row, matrix2_col))
    return product

def vector_dot_product(vector1, vector2):
    assert len(vector1) == len(vector2), 'Expected Vectors of Equal Length'

    return sum([vector1[i]*vector2[i] for i in range(len(vector1))])

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))
```

---

## Q
What is the **Transpose** of a matrix?

## A
A transposed matrix is rotated such that its rows are the columns of the original and its columns are the rows of the original.

---

## Q
What is a **Square Matrix**? What are some examples?

----

## Q
How do we find the **Determinant** of a Matrix?

## A
The **determinant** is a property that all *square* matrices possess, denoted with pipes (i.e. |A|).

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

## Q
What is the **Inverse** of a matrix? What happens if we multiply a matrix by its inverse? What is this important in data science?

---

## Q
What is **Variance**?

## A
The average of the squared differences from the Mean.

----

## Q
What is **Standard Deviation**?

## A
A measure of how spread out numbers are.

---

## Q
What is **Covariance**?

## A
In probability theory and statistics, covariance is a measure of the joint variability of two random variables. If the greater values of one variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values, (i.e., the variables tend to show similar behavior), the covariance is positive.

----

## Q
What is **Singular Value Decomposition**?

## A
Factorization of a real or complex matrix. It is the generalization of the eigendecomposition of a given matrix using its constituent elements. These constituent parts help make certain subsequent matrix calculations simpler.

----

## Q
What is **Orthogonality**?

## A
Orthogonality is the property that means 'changing A does not change B'. An example of an orthogonal system would be where we skip to the next song on our playlist, and changing the song does not change the volume.

In programming, orthogonality means that when we execute an instruction, nothing but that instruction happens.

----

## Q
What is a **Linear Combination**?

## A
In linear algebra, we define the concept of linear combinations in terms of vectors. But, it is actually possible to talk about linear combinations of anything...

(scalar)(something 1 ) + (scalar)(something 2) + (scalar)(something 3)

These 'somethings' could be everyday variables like x, y, z etc. or something more complicated like polynomials. A linear combination is a particular way of combining things (variables, vectors, etc.) using scalar multiplication and addition.

----

## Q
What is **Collinearity**? Why can it be a problem?

## A
Collineartiy is a condition in which some of the independent variables are highly correlated.

Collinearity tends to inflate the variance of at least one estimated regression coefficient.

----

## Q
What are some basic applications of linear algebra in Data Science?

## A
* Vectors: Rows, Columns, Lists, Arrays
* Matrices: Tables, Spreadsheets, DataFrames
* Linear Modeling: Linear Regression, Logistic Regression, Gradient Descent, etc.

----

## Q
What is **Principal Component Analysis**?

## A
Principal Component Analysis(or PCA for short), is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of linearly uncorrelated variables called principal components.

----
