class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        marked_row = [-1 for i in range(len(A))]
        marked_column = [-1 for i in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    marked_row[i] = 0
                    marked_column[j] = 0
        print(marked_row, marked_column)
        # marking row
        for index, value in enumerate(marked_row):
            if value > -1:
                A[index] = [0 for _ in range(len(A[0]))]

        # marking column
        for index, value in enumerate(marked_column):
            if value > -1:
                for i in range(len(A)):
                    A[i][index] = 0

        return A


if __name__ == "__main__":
    mat = [
        [97, 18, 55, 1, 50, 17, 16, 0, 22, 14]
        , [58, 14, 75, 54, 11, 23, 54, 95, 33, 23]
        , [73, 11, 2, 80, 6, 43, 67, 82, 73, 4]
        , [61, 22, 23, 68, 23, 73, 85, 91, 25, 7]
        , [6, 83, 22, 81, 89, 85, 56, 43, 32, 89]
        , [0, 6, 1, 69, 86, 7, 64, 5, 90, 37]
        , [10, 3, 11, 33, 71, 86, 6, 56, 78, 31]
        , [16, 36, 66, 90, 17, 55, 27, 26, 99, 59]
        , [67, 18, 65, 68, 87, 3, 28, 52, 9, 70]
        , [41, 19, 73, 5, 52, 96, 91, 10, 52, 21]
    ]
    result = Solution().solve(mat)

    for i in range(len(mat)):
        print(*mat[i])
