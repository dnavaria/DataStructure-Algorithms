class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        min_so_far = float("inf")
        ptr = 0

        # find minimum window
        min_window = 0
        for i in A:
            min_window += 1 if i <= B else 0

        bad = 0
        for i in range(min_window):
            bad += 1 if A[i] > B else 0

        if bad < min_so_far:
            min_so_far = bad

        if bad == 0:
            return 0

        ptr = 0
        for i in range(min_window, len(A)):
            if A[ptr] > B:
                bad -= 1
            ptr += 1
            if A[i] > B:
                bad += 1

            if bad < min_so_far:
                min_so_far = bad

        return min_so_far