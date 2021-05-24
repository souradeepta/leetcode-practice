from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        result = []
        output = 0
        maximum = float('-inf')
        for i in range(len(rectangles)):
            result.append((min(rectangles[i][0], rectangles[i][1])))
        maximum = max(result)
        for ele in result:
            if ele == maximum:
                output += 1
        return output


s = Solution()
assert 3 == s.countGoodRectangles(
    [[5, 8], [3, 9], [5, 12], [16, 5]]), "incorrect output"

s = Solution()
assert 3 == s.countGoodRectangles(
    [[2, 3], [3, 7], [4, 3], [3, 7]]),  "incorrect output"
