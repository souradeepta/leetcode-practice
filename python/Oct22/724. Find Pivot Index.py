class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (total - x - leftsum):
                return i
            leftsum += x
        return -1


s = Solution()
assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
assert s.pivotIndex([1, 2, 3]) == -1
assert s.pivotIndex([2, 1, -1]) == 0
