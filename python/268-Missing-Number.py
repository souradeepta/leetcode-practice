from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        sumOfLen = length*(length+1)//2
        sumOfList = sum(nums)
        ans = sumOfLen - sumOfList
        ans if ans else max(nums) + 1
        return ans


obj = Solution()
print(f'{obj.missingNumber([9,6,4,2,3,5,7,0,1])}')
