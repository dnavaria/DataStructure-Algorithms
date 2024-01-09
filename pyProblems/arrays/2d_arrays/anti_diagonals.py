class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        i = 0
        result = []
        for j in range(len(A)):
            s = i
            e = j
            arr = [0] * len(A)
            index = 0
            while s < len(A) and e >= 0:
                arr[index] = A[s][e]
                s += 1
                e -= 1
                index += 1
            result.append(arr)

        j = len(A) - 1
        for i in range(1, len(A)):
            arr = [0] * len(A)
            s = i
            e = j
            index = 0
            while s < len(A) and e >= 0:
                arr[index] = A[s][e]
                s += 1
                e -= 1
                index += 1
            result.append(arr)
        return result
