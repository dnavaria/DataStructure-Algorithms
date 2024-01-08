class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        max_so_far = 0
        for i in range(len(C)):
            s = 0
            for j in range(i, len(C)):
                s += C[j]
                if s <= B:
                    max_so_far = max(s, max_so_far)
        return max_so_far
