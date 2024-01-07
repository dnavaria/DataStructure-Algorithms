class Solution:
    # @param A : list of integers
    # @return an integer
    # You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.
    # The first argument is an integer array A.
    # Return the second largest element. If no such element exist then return -1.
    def solve(self, A):
        if len(A) <= 1:
            return -1
        max_element = A[0]
        second_max = -1
        for i in range(1, len(A)):
            if max_element > A[i] > second_max:
                second_max = A[i]
            elif A[i] > max_element and A[i] > second_max:
                second_max = max_element
                max_element = A[i]
        return -1 if max_element == second_max else second_max


# print(Solution().solve(A=[13, 7, 16, 18, 14, 17, 18, 8, 10]))
print(Solution().solve(A=[2,1,2]))
