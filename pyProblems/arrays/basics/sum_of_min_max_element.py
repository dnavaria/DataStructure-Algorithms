class Solution:
    # @param A : list of integers
    # @return an integer
    # Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.
    # First argument A is an integer array.
    # Return the sum of maximum and minimum element of the array
    def solve(self, A):
        min_element = float("inf")
        max_element = float("-inf")

        for i in range(len(A)):
            current_element = A[i]
            max_element = current_element if current_element > max_element else max_element
            min_element = current_element if current_element < min_element else min_element

        return min_element + max_element


result = Solution().solve([1, 2, -1, 4, 5, -2, -3])
print(result)
