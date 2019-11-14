# 3Sum
# Two Pointer:  Time:O(NlogN+N^2)~=O(N^2), Space:O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sort the list
        nums.sort()

        length = len(nums)

        for i in range(length-2):
            # since list is sorted, first number if +ve, then impossible to get 0
            if nums[i]>0:
                break
            
            # ignoring if the number is same
            if i>0 and nums[i] == nums[i -1]:
                continue

            # since we are already convering i in our for
            left, right = i+1, length-1

            while left < right:
                total = nums[i]+nums[left]+nums[right]

                if total < 0:
                    left = left + 1
                elif total > 0:
                    right = right - 1
                else:
                    # here we get a match
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # move left and right such that same value 
                    # numbers are ignored. Since list is sortee
                    while left < right and nums[left] == nums [left + 1]:
                        left = left + 1
                    while left <right and nums[right] == nums [right - 1]:
                        right = right - 1

                    left = left + 1
                    right = right - 1
        
        return result