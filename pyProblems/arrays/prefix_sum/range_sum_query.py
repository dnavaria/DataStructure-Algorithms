class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        # create a prefix array
        result = []
        prefix = [0] * len(A)
        prefix[0] = A[0]
        for i in range(1, len(A)):
            prefix[i] = prefix[i-1] + A[i]
        for i in range(len(B)):
            s = B[i][0]
            e = B[i][1]
            if s == 0:
                result.append(prefix[e])
            else:
                sum_val = prefix[e] - prefix[s-1]
                result.append(sum_val)
        return result


print(Solution().rangeSum([1, 2, 3, 4, 5], [[0, 3], [1, 2]]))
