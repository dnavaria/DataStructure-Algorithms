class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count_of_a = 0
        pairs = 0
        MOD = 1000*1000*1000 + 7
        for i in range(len(A)):
            if A[i] == "A":
                count_of_a += 1
            elif A[i] == "G":
                pairs += count_of_a
        return pairs % MOD