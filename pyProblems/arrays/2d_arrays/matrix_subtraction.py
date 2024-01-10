class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        result = []
        for i in range(len(A)):
            diff = []
            for j in range(len(A[0])):
                diff.append(A[i][j] - B[i][j])
            result.append(diff)
        return result
