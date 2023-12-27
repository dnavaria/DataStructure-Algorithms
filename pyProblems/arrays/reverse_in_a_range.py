class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        while B < C:
            A[B], A[C] = A[C], A[B]
            B += 1
            C -= 1
        return A
