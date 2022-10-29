class Solution:
    def maxArea(self, height: list[int], type=0) -> int:
        """You are given an integer array height of length n.
                There are n vertical lines drawn such that the two endpoints
                of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container,
        such that the container contains the most water.

                Args:
                    height (list[int]): _description_

                Returns:
                    int: _description_
                Complexity:
                Time O(n)
                Space O(1)
        """
        left, right = 0, len(height) - 1
        area = 0
        if type == 0:
            while left < right:
                if height[left] < height[right]:
                    area = max(area, (right - left) * (height[left]))
                    left += 1
                else:
                    # note not elif here because it also
                    # handles when left and right heights are
                    # same
                    area = max(area, (right - left) * (height[right]))
                    right -= 1
        else:
            # neetcode
            while left < right:
                area = max(area, (right - left) * min(height[left], height[right]))
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
        return area


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7], type=1) == 49
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([0, 2]) == 0
