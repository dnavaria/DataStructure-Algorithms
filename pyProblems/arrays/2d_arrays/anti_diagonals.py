class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        def traverse_downwards_diagonally(s, e, N, A):
            diagonal = [0] * N
            s = s
            e = e
            ptr = 0
            while s < N and e >= 0:
                diagonal[ptr] = A[s][e]
                s += 1
                e -= 1
                ptr += 1
            return diagonal

        result = []
        N = len(A[0])

        for j in range(N):
            temp = traverse_downwards_diagonally(s=0, e=j, N=N, A=A)
            result.append(temp)

        for i in range(1, N):
            temp = traverse_downwards_diagonally(s=i, e=N - 1, N=N, A=A)
            result.append(temp)
        return result


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    resultant_matrix = Solution().diagonal(A=mat)
    for i in resultant_matrix:
        print(*i)
