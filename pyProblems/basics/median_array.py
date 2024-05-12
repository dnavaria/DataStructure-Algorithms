from math import floor
class Solution:
    def find_median(self, v):
        v.sort()
        length = len(v)
        if length % 2 == 0:
            return floor((v[length // 2] + v[length // 2 - 1] ) / 2)
        else:
            return v[length // 2]

# print(Solution().find_median([90,100,78,89,67]))
print(Solution().find_median([56,67,30,79]))