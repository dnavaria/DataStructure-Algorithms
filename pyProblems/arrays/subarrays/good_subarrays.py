class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        good_sub_arrays = 0
        for i in range(len(A)):
            s = 0
            for j in range(i, len(A)):
                s += A[j]
                current_length = (j + 1) - i
                if (current_length % 2 == 0 and s < B) or (current_length % 2 == 1 and s > B):
                    good_sub_arrays += 1
        return good_sub_arrays
