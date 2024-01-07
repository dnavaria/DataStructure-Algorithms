class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        last_min_index = -1
        last_max_index = -1
        ans = len(A)
        min_element = min(A)
        max_element = max(A)
        for i in range(len(A)):
            if A[i] == min_element:
                last_min_index = i
                if last_max_index != -1:
                    ans = min(ans, last_min_index - last_max_index + 1)

            if A[i] == max_element:
                last_max_index = i
                if last_min_index != -1:
                    ans = min(ans, last_max_index - last_min_index + 1)
        return ans

