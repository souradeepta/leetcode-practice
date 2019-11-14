#Two Sum
# Brute-force:: Time: O(n^2), Space: O(1)
# One-pass Hash table:: Time O(n), Space: O(n) 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # always check for empty input
        if len(nums) == 0:
            return []
            
        index = {}
        for i in range(0, len(nums)):
            compliment = target - nums[i]
            if ((compliment) in index):
                return [i, index[compliment]]
            else:
                index[nums[i]] = i
