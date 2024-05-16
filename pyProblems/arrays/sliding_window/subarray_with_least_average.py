class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        current_sum = 0
        for i in range(B):
            current_sum += A[i]

        min_so_far = current_sum
        index = 0
        for i in range(B, len(A)):
            current_sum = (current_sum + A[i]) - A[i - B]
            if current_sum < min_so_far:
                min_so_far = current_sum
                index = i - B + 1

        return index