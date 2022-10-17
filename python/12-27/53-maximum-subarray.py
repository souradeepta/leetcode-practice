class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        global_max = nums[0]
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            global_max = max(global_max, current_sum)
        return global_max
        # global_max = 0
        # for i in range(len(nums)):
        #     local_maxima = 0
        #     current_sum = 0
        #     for j in range(i, len(nums)):
        #         current_sum = current_sum+ nums[j]
        #         local_maxima = max(current_sum, local_maxima)
        #     global_max = max(global_max, local_maxima)
        # pass

    def test_maxSubArray(self):
        assert(self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
        assert(self.maxSubArray([1]) == 1)
        assert(self.maxSubArray([5,4,-1,7,8]) == 23)

s = Solution()
s.test_maxSubArray()