## Q
What is **Orthogonality**? How do we tell whether two vectors are orthogonal?

## A
Orthogonality is another word for "perpendicularity". Two vectors or matrices that are perpendicular to one another are orthogonal.

Two vectors are orthogonal to each other if their dot product is zero.

----

## Q
What are **Unit Vectors**? How to we convert a vector to a **Unit Vectors**?

## A
**Unit Vectors** are vetors of length (or norm) equal to 1. Likewise, we may convert a vector to its unit vector by dividing the vector by its norm.

----

## Q
What is a **Linear Combination**?

## A
Any vector (or matrix) can be be described in terms of a linear combination of scaled unit vectors. In other words, the multiplication of a scalar (or vector of scalars) by a unit vector (or matrix of unit vetors).

----

## Q
What is **Collinearity**? Why can it be a problem?

## A
Collineartiy is a condition in which some of the independent variables are highly correlated.

Collinearity tends to inflate the variance of at least one estimated regression coefficient.

----

## Q
What is **Span**?

## A
The span is the set of all possible vectors that can be created with a linear combination of vectors.

----

## Q
What are **Linearly Dependent Vectors**?

## A
Two or more vectors that live on the same line are linearly dependent. This means that there is no linear combination that will create a vector that lies outside of that line. In this case, the span of these vectors is the line that they lie on.

----

## Q
What is **Linearly Independent Vectors**?

## A
Linearly independent vectors are vectors that don't lie on the same line as each other. If two vectors are linearly independent, then there ought to be some linear combination of them that could represent any vector in the space.

----

## Q
What is a **Basis**?

## A
The basis of a vector space *V* is a set of vectors that are linearly independent and that span the vector space *V*. A set of vectors spans a space if their linear combinations fill the space.

----

## Q
What is an **Orthogonal Basis**?

## A
An orthogonal basis is a set of vectors that are linearly independent, span the vector space, and are orthogonal to each other.

----

## Q
What is an **Orthonormal Basis**?

## A
An orthonormal basis is a set of vectors that are linearly independent, span the vector space, are orthogonal to eachother and each have unit length.

The unit vectors form an orthonormal basis for whatever vector space that they are spanning.

----

## Q
What is **Rank**?

## A
The rank of a matrix is the dimension of the vector space spanned by its columns. Just because a matrix has a certain number of rows or columns (dimensionality) doesn't neccessarily mean that it will span that dimensional space. Sometimes there exists a sort of redundancy within the rows/columns of a matrix (linear dependence) that becomes apparent when we reduce a matrix to row-echelon form via Gaussian Elimination.

----

## Q
What is **Gaussian Elimination**?

## A
Gaussian Elimination is a process that seeks to take any given matrix and reduce it down to what is called "Row-Echelon form." A matrix is in Row-Echelon form when it has a 1 as its leading entry (furthest left) in each row, and zeroes at every position below that main entry. These matrices will usually wind up as a sort of upper-triangular matrix (not necessarly square) with ones on the main diagonal.

----

## Q
What is **Projection**?

## A

----

## Q
What is **Principal Component Analysis**?

## A
Principal Component Analysis(or PCA for short), is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of linearly uncorrelated variables called principal components.