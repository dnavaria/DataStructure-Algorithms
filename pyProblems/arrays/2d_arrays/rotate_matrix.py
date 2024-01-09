class Solution:
    # @param A : list of list of integers

    def transpose(self, A):
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]

    def solve(self, A):
        self.transpose(A)
        for i in range(len(A)):
            A[i] = reversed(A[i])
        return A
