class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        leaders = 1
        max_element = A[-1]
        result = [max_element]
        for i in range(len(A) - 2, -1, -1):
            if A[i] > max_element:
                leaders += 1
                max_element = A[i]
                result.append(max_element)
        return result
