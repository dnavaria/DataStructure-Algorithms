class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers

    def solve_extra_space(self, A):
        row_wise = [0] * len(A)
        col_wise = [0] * len(A)

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    row_wise[i] = -1
                    col_wise[j] = -1

        for i in range(len(A)):
            for j in range(len(A[0])):
                if row_wise[i] == -1 or col_wise[j] == -1:
                    A[i][j] = 0
        return A

    def solve(self, A):
        for i in range(len(A)):
            flag = False
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    flag = True
            if flag:
                for j in range(len(A[0])):
                    if A[i][j] != 0:
                        A[i][j] = -1

        for j in range(len(A)):
            flag = False
            for i in range(len(A[0])):
                if A[i][j] == 0:
                    flag = True
            if flag:
                for i in range(len(A[0])):
                    if A[i][j] != 0:
                        A[i][j] = -1

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == -1: A[i][j] = 0
        return A