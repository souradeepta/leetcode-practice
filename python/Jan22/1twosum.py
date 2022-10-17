class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        compliment = {}
        for i in range(len(nums)):
            if target - nums[i] in compliment:
                return [compliment[target - nums[i]], i]
            else:
                compliment[nums[i]] = i

    def test_twoSum(self):
        assert(self.twoSum([2,7,11,15], 9) == [0,1])
        assert(self.twoSum([3,2,4], 6) == [1,2])

s =Solution()

s.test_twoSum()