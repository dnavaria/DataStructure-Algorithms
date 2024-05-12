class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        t_matrix = [[0 for i in range(N)] for j in range(M)]
        for i in range(M):
            for j in range(N):
                t_matrix[i][j] = A[j][i]
        return t_matrix

