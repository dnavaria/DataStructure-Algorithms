class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        N = len(A)
        # finding first window sum
        current_sum = 0
        for i in range(B):
            current_sum += A[i]
        ptr = 0
        for i in range(B, N):
            current_sum -= A[ptr]
            ptr += 1
            current_sum += A[i]

        if current_sum == C:
            return 1

        return 0
