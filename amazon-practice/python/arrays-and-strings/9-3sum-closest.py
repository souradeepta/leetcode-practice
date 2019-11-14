class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        total = 0

        # init result
        result = sum(nums[:3])

        length = len(nums) - 1

        nums.sort()

        for i in range(length):
            left, right = i + 1 , length
            while left< right:
                total = nums[i] + nums[left] + nums[right] 
                if abs(total-target) < abs(result-target):
                    result = total

                # look for bigger numbers
                if total < target:
                    left = left + 1
                # look for smaller numbers
                elif total > target:
                    right = right - 1 
                # found number
                else:
                    return result
        return result
