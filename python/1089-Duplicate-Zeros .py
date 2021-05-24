# 1089. Duplicate Zeros
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return None
        length = len(arr)
        i, j = 0, 0
        ans = []
        for i in range(length):
            if arr[i] == 0:
                ans[j] = 0
                j+=1
                ans[j] = 0
            else:
                ans[j] = arr[i]
                # i+=1
            j+=1
        return ans
            # arr = ans
s = Solution()
input = [1,0,2,3,0,4,5,0]
s.duplicateZeros(input)
print(input)
