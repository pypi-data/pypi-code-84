'''
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and 
column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''

def transpose(A):
    matrix = [[None for _ in range(len(A))] for _ in range(len(A[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = A[j][i]

    return matrix 