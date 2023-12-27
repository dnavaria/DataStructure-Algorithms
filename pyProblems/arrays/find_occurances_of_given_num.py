class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # Given an array A and an integer B, find the number of occurrences of B in A.
    # Given an integer array A and an integer B.
    # Return an integer, number of occurrences of B in A.
    def solve(self, A, B):
        num_frequency = 0
        for i in range(len(A)):
            if A[i] == B:
                num_frequency += 1
        return num_frequency


print(Solution().solve([1, 2, 2, 3, 2, 5, 4, 2], 2))
