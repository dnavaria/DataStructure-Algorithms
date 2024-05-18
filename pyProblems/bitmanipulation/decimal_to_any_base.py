class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def DecimalToAnyBase(self, A, B):
        quo = A
        result = 0
        power = 1
        while quo > 0:
            result = result + (int(quo % B)) * power
            power *= 10
            quo /= B
        return result

