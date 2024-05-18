class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        result = 0
        ptr = 0
        while A > 0:
            digit = int(A % 10)
            powered_base = int(B ** ptr)
            value = (digit * powered_base)
            result += value
            ptr += 1
            A /= 10
        return result
