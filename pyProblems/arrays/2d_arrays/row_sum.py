class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        result = []
        for i in range(len(A)):
            result.append(sum(A[i]))
        return result
