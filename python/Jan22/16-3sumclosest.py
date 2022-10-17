class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total
                if abs(total - target) < abs(result - target):
                    result = total

                if total < target:
                    j += 1

                if total > target:
                    k -= 1

        return result

    def test(self):
        assert self.threeSumClosest([-1, 2, 1, -4], 1)


s = Solution()
s.test()
