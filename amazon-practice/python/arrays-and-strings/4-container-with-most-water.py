# Container with most water
# Brute force:: Time:O(n), Space:O(1)
# Two pointer:: Time
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = left = 0
        right = len(height) - 1

        while (left < right):
            maxArea = max(maxArea, min(height[left], height[right]) * (right - 1))

            if (height[left] < height[right]):
                left = left + 1 
            else:
                right = right - 1
            
        return maxArea
