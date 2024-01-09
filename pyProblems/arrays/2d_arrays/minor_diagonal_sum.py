class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        i = 0
        j = len(A[0]) - 1
        diagonalSum = 0
        while i < len(A) and j > -1:
            diagonalSum += A[i][j]
            i += 1
            j -= 1
        return diagonalSum
