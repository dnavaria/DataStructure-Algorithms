class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    # Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.
    # The first argument given is the integer array A.
    # The second argument given is the integer B.
    # Return the array A after rotating it B times to the right

    @staticmethod
    def reverse_in_a_range(A, i, j):
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    def solve(self, A, B):
        if B == len(A):
            return A
        B = B % len(A)
        self.reverse_in_a_range(A=A, i=0, j=len(A) - 1)
        self.reverse_in_a_range(A=A, i=0, j=B - 1)
        self.reverse_in_a_range(A=A, i=B, j=len(A) - 1)
        return A


print(Solution().solve(A=[1, 2, 3, 4], B=2))
# print(Solution().solve(A=[7, 4, 2, 10, 5], B=10))
# print(Solution().solve(A=[1, 1, 4, 9, 4, 7, 1], B=9))
