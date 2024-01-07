class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        count_of_substrings = 0
        for i in range(len(A)):
            if A[i] in vowels:
                length_of_rest_of_the_array = len(A) - i
                count_of_substrings += length_of_rest_of_the_array

        return count_of_substrings