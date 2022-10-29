class Solution:
    def productExceptSelf(self, nums: list[int], type=0) -> list[int]:
        """as the problem states on nums

        Args:
            nums (list[int]): _description_
            type (int, optional): _description_. Defaults to 0.

        Returns:
            list[int]: _description_
        Complexity:
        Time O(n)
        Space O

        """
        prefix_prod, suffix_prod = [1] * len(nums), 1
        size = len(nums)
        if type == 0:
            for i in range(1, size):
                prefix_prod[i] = prefix_prod[i - 1] * nums[i - 1]
            for i in range(size - 1, -1, -1):
                prefix_prod[i] *= suffix_prod
                suffix_prod *= nums[i]
        return prefix_prod


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert s.productExceptSelf([1, 1]) == [1, 1]
