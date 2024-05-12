class Solution:
    # Complete this function

    def printN(self, N):
        if N == 0:
            return
        self.printN(N - 1)
        print(N, end=" ")

    def printNos(self, N):
        self.printN(N)


Solution().printNos(10)
