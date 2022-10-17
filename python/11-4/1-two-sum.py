input = [2, 7, 11, 15]
target = 9
output = [0, 1]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return None
        compliment = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] not in compliment:
                compliment[comp] = i
            else:
                return [compliment[nums[i]], i]


s = Solution()
assert s.twoSum(input, target) == output
