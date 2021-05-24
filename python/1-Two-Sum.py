from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i in range(len(nums)):
            if nums[i] not in compliment:
                compliment[target - nums[i]] = i
            else:
                return [compliment[nums[i]], i]


s = Solution()
result = s.twoSum([2, 7, 11, 15], 9)
result2 = s.twoSum([3,2,4], 6)
result3 = s.twoSum(([3, 3]), 6)

print(result, result2, result3)
