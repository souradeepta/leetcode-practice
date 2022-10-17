from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = sum + nums[i]
            sum = nums[i]
        # print(nums)
        return nums


s = Solution()
assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
