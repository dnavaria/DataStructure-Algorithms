class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix = [0] * len(A)
        prefix[0] = A[0]

        for i in range(1, len(A)):
            prefix[i] = prefix[i - 1] + A[i]

        for i in range(len(A)):
            left_sum = 0 if i == 0 else prefix[i-1]
            right_sum = prefix[-1] - prefix[i]
            if left_sum == right_sum:
                return i

        return -1
