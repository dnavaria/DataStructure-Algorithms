class Solution:
    # @param A : list of integers
    # @return an integer
    # Given an integer array A of size N. In one second, you can increase the value of one element by 1.
    # Find the minimum time in seconds to make all elements of the array equal.
    # First argument is an integer array A.
    # Return an integer denoting the minimum time to make all elements equal.
    def solve(self, A):
        max_element = max(A)
        time_in_seconds = 0
        for i in range(len(A)):
            if A[i] == max_element:
                continue
            time_in_seconds += (max_element - A[i])
        return time_in_seconds


print(Solution().solve(A=[2, 4, 1, 3, 2]))
