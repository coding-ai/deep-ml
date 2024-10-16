# Transpose of a Matrix (easy)

## [Problem Description](https://www.deep-ml.com/problem/Transpose%20of%20a%20Matrix)

The goal is to compute the transpose of a given matrix. The transpose is obtained by flipping rows and columns. If the matrix is empty, the function will return `-1` to indicate that the operation cannot be performed.

## Transpose Definition

For a matrix $A$ with $m$ rows and $n$ columns, the transpose of $A$ is a matrix $B$ with $n$ rows and $m$ columns, where each element of $B$ is defined as:

$$
B_{ij} = A_{ji}
$$

Where:
- $A_{ji}$ is the element at the $j$-th row and $i$-th column of the matrix $A$,
- $B_{ij}$ is the element at the $i$-th row and $j$-th column of the matrix $B$.

### Example

#### Input:

Matrix $A$:

$$
A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

#### Calculation:

1. The first column of matrix $A$ becomes the first row of the transposed matrix:

$$
B_1 = \begin{bmatrix} 1 & 4 \end{bmatrix}
$$

2. The second column of matrix $A$ becomes the second row of the transposed matrix:

$$
B_2 = \begin{bmatrix} 2 & 5 \end{bmatrix}
$$

3. The third column of matrix $A$ becomes the third row of the transposed matrix:

$$
B_3 = \begin{bmatrix} 3 & 6 \end{bmatrix}
$$

#### Output:

The resulting transposed matrix $B$ is:

$$
B = \begin{bmatrix} 
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix}
$$

#### Edge Case: Empty Matrix

If the matrix is empty (i.e., it has no rows), the function returns `-1`.