class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        prefix = [1] * len(A)
        prefix[0] = A[0]
        for i in range(1, len(A)):
            prefix[i] = prefix[i - 1] * A[i]

        suffix = [1] * len(A)
        suffix[-1] = A[-1]
        for i in range(len(A) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * A[i]

        # print(prefix)
        # print(suffix)
        result = []
        for i in range(len(A)):
            if i == 0:
                result.append(suffix[i+1])
            elif i == len(A) - 1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * suffix[i+1])
        return result
# Solution().solve(range(1, 6))
