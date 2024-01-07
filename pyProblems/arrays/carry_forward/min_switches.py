class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        min_switch = 0
        flipped = False
        for i in range(len(A)):
            if not flipped:
                if A[i] == 0:
                    flipped = True
                    min_switch += 1
            else:
                if A[i] == 1:
                    flipped = False
                    min_switch += 1
        return min_switch

