from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if (sum(nums[:i-1]) == sum(nums[i:])):
                return i - 1
        return -1


obj = Solution()
print(f'{obj.pivotIndex([-1,-1,0,1,1,0])}')
