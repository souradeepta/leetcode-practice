import pytest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """find indices of sum of numbers in num to target

        Args:
            nums (list[int]): _description_
            target (int): _description_

        Raises:
            ValueError: _description_

        Returns:
            list[int]: _description_
        Complexity:
            Time O(n)
            Space O(n)
        """
        compliment = {}
        for i, n in enumerate(nums):
            comp = target - nums[i]
            if comp in compliment:
                return [compliment[comp], i]
            else:
                compliment[nums[i]] = i
        raise ValueError("no solution found")


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    with pytest.raises(ValueError):
        s.twoSum([], 6)
