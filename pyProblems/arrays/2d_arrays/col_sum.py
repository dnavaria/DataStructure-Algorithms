class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        result = []
        col = len(A[0])
        for i in range(col):
            s = 0
            for j in range(len(A)):
                s += A[j][i]
            result.append(s)
        return result
