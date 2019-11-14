# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 2 * sum(set(nums)) -sum(nums)
        return ans