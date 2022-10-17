class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        compliment = {}
        for i in range(len(nums)):
            if nums[i] not in compliment:
                compliment[target-nums[i]] = i
            else:
                return [compliment[nums[i]], i]
        pass

    def test_twoSum(self):
        assert self.twoSum([2, 7, 11, 15], 9) == [0, 1]
        assert self.twoSum([3, 2, 4], 6) == [1, 2]
        assert self.twoSum([3, 3], 6) == [0, 1]

s = Solution()
s.test_twoSum()