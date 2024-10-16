# Matrix times Vector (easy)

## [Problem Description](https://www.deep-ml.com/problem/Matrix%20times%20Vector)

The goal is to compute the dot product between a matrix and a vector. This operation is possible when the number of columns in the matrix is equal to the number of elements in the vector. If the dimensions do not match, the function will return `-1` to indicate that the operation is not possible.


## Dot Product Definition

For a matrix $A$ with $m$ rows and $n$ columns, and a vector $b$ with $n$ elements, the dot product of each row of the matrix with the vector is calculated as:

$$
c_i = \sum_{j=1}^{n} A_{ij} \times b_j
$$

Where:
- $A_{ij}$ is the element at the $i$-th row and $j$-th column of the matrix $A$,
- $b_j$ is the $j$-th element of the vector $b$,
- $c_i$ is the result of the dot product for the $i$-th row.

### Example

#### Input:

Matrix $A$:

$$
A = \begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 5 \\
6 & 8 & 9
\end{bmatrix}
$$

Vector $b$:

$$
b = \begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
$$

#### Calculation:

1. For the first row of the matrix:

$$
c_1 = (1 \times 1) + (2 \times 2) + (3 \times 3) = 14
$$

2. For the second row of the matrix:

$$
c_2 = (2 \times 1) + (4 \times 2) + (5 \times 3) = 25
$$

3. For the third row of the matrix:

$$
c_3 = (6 \times 1) + (8 \times 2) + (9 \times 3) = 50
$$

#### Output:

The resulting vector $c$ is:

$$
c = \begin{bmatrix} 14 \\ 25 \\ 50 \end{bmatrix}
$$

#### Edge Case: Mismatched Dimensions

If the matrix and vector have incompatible dimensions (i.e., the number of columns in the matrix does not equal the number of elements in the vector), the function returns `-1`.