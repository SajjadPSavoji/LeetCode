# 311. Sparse Matrix Multiplication
# Solved
# Medium

# Topics
# conpanies icon
# Companies
# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

# Example 1:


# Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
# Output: [[7,0,0],[-7,0,3]]
# Example 2:

# Input: mat1 = [[0]], mat2 = [[0]]
# Output: [[0]]
 

# Constraints:

# m == mat1.length
# k == mat1[i].length == mat2.length
# n == mat2[i].length
# 1 <= m, n, k <= 100
# -100 <= mat1[i][j], mat2[i][j] <= 100


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        
        # Store non-zero entries of mat1: row -> list of (col, value)
        nz1 = [[] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    nz1[i].append((j, mat1[i][j]))
        
        # Store non-zero entries of mat2: row -> list of (col, value)
        nz2 = [[] for _ in range(k)]
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    nz2[i].append((j, mat2[i][j]))
        
        # Result matrix
        res = [[0] * n for _ in range(m)]
        
        # Multiply only non-zero pairs
        for i in range(m):
            for t, v1 in nz1[i]:
                for j, v2 in nz2[t]:
                    res[i][j] += v1 * v2
        
        return res

