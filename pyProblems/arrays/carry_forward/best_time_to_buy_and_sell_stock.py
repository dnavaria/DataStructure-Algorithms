class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit_with_suffix_array(self, A):
        if len(A) == 0:
            return 0
        suffix = [0] * len(A)
        suffix[-1] = A[-1]
        for i in range(len(A) - 2, -1, -1):
            suffix[i] = max(suffix[i+1], A[i])
        max_profit = 0
        for i in range(len(A)-1):
            if (suffix[i+1] - A[i]) > max_profit:
                max_profit = suffix[i+1] - A[i]
        return max_profit
    def maxProfit(self, A):
        if len(A) == 0:
            return 0
        max_profit = 0
        min_val = A[0]
        for i in range(1, len(A)):
            min_val = min(A[i], min_val)
            current_profit = A[i] - min_val
            max_profit = max(max_profit, current_profit)
        return max_profit



Solution().maxProfit([1, 4, 5, 2, 4])
