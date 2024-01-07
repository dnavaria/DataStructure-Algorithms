class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        prefix = [0] * len(A)
        for i in range(len(A)):
            if A[i] % 2 == 0:
                prefix[i] = 1

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]

        result = []
        for i in range(len(B)):
            s = B[i][0]
            e = B[i][1]
            if s == 0:
                result.append(prefix[e])
            else:
                result.append(prefix[e] - prefix[s-1])
        return result