class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for i in range(len(A)):
            s = 0
            for j in range(i, len(A)):
                s+=A[j]
                if s < B:
                    count+=1
        return count