class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Two Sum II - Input Array Is Sorted

        Args:
            numbers (list[int]): _description_
            target (int): _description_

        Returns:
            list[int]: _description_
            Two pointers: O(n) time and O(1) space
        """
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] == target:
                return [l+1, r+1]
            else:
                l += 1


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]
