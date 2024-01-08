class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        result = []
        for i in range(len(A)):
            for j in range(i, len(A)):
                result.append(A[i:j + 1])
        return result
