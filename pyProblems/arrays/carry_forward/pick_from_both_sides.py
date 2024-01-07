class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        prefix = [0] * len(A)
        prefix[0] = A[0]
        for i in range(1, len(A)):
            prefix[i] = prefix[i-1] + A[i]
        suffix = [0] * len(A)
        suffix[-1] = A[-1]
        for i in range(len(A)-2, -1, -1):
            suffix[i] = suffix[i+1] + A[i]

        maximum = max(prefix[B-1], suffix[len(A)-B])
        for j in range(1, B):
            maximum = max(maximum, prefix[j-1] + suffix[len(A)-B+j])
        return maximum
