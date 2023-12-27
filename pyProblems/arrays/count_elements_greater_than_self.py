class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(A):
        count = 0
        for i in range(len(A)):
            for j in range(len(A)):
                if A[j] > A[i]:
                    count += 1
                    break
        return count

    def solve_optimized(self, A):
        max_element = 0
        for i in range(len(A)):
            if A[i] > max_element:
                max_element = A[i]
        max_element_occurances = 0
        for i in range(len(A)):
            if A[i] == max_element:
                max_element_occurances += 1
        return len(A) - max_element_occurances
