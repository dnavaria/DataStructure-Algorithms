class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        i = 0
        j = len(A) - 1
        new_arr = [0] * len(A)
        while i <= j:
            new_arr[i] = A[j]
            new_arr[j] = A[i]
            i += 1
            j -= 1
        return new_arr
