# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x//2+1):
            if i*i >= x:
                return i

s = Solution()
assert(s.mySqrt(4)) == 2
# print(s.mySqrt(8))
assert(s.mySqrt(8)) == 2
