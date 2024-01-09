class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        diagonal_sum = 0
        for i in range(0, N):
            diagonal_sum += A[i][i]
        return diagonal_sum



