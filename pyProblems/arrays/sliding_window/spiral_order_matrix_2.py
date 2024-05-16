class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        flow_x = 0
        flow_y = 0

        matrix = [[0 for _ in range(A)] for _ in range(A)]

        ptr = 1
        N = A
        while ptr <= A * A:
            i, j = flow_x, flow_y

            # forward
            while j < N:
                matrix[i][j] = ptr
                ptr += 1
                j += 1
            i += 1
            j -= 1

            # downward
            while i < N:
                matrix[i][j] = ptr
                ptr += 1
                i += 1
            j -= 1
            i -= 1

            # backward
            while j >= flow_x:
                matrix[i][j] = ptr
                ptr += 1
                j -= 1
            j += 1
            i -= 1

            # upward
            while i > flow_y:
                matrix[i][j] = ptr
                ptr += 1
                i -= 1

            flow_x += 1
            flow_y += 1
            N -= 1
        return matrix


if __name__ == '__main__':
    result = Solution().generateMatrix(5)
    for row in result:
        print(*row)
