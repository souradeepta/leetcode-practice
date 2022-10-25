class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i, n in enumerate(nums):
            if leftsum == (total - n - leftsum):
                return i
            leftsum += n
        return -1


s = Solution()
assert s.findMiddleIndex([2, 3, -1, 8, 4]) == 3
assert s.findMiddleIndex([1, -1, 4]) == 2
assert s.findMiddleIndex([2, 5]) == -1
