class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        for i in range(N):
            for j in range(i + 1, N):
                if i == j:
                    continue
                else:
                    temp = A[i][j]
                    A[i][j] = A[j][i]
                    A[j][i] = temp
        return A
