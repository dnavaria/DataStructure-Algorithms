class Solution:
    # @param A : list of integers
    # @return an long
    def subarraySum_brute_force(self, A):
        sum_value = 0
        for i in range(len(A)):
            s = 0
            for j in range(i, len(A)):
                s += A[j]
                sum_value += s
        return sum_value

    def subarraySum(self, A):
        sum_value = 0
        for i in range(len(A)):
            start = i + 1
            end = len(A) - i
            contribution = (start * end) * A[i]
            sum_value += contribution
        return sum_value
