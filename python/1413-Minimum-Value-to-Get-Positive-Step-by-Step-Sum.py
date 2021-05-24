from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # can use 0 as ref startValue
        result = 0
        test = []
        for ele in nums:
            result += ele
            # print(result)
            test.append(result)
        ans = abs(min(test))+1 if min(test) < 0 else 1
        return ans


obj = Solution()
# print(f'{obj.minStartValue([-3,2,-3,4,2])}')
print(f'{obj.minStartValue([1,-2,-3])}')
# print(f'{obj.minStartValue([-3,23343])}')

# print(f'{obj.minStartValue([3,-23343])}')
