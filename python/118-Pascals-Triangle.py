"""[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
[1,5,10,10,5,1]
]
    """
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 1. need a list of list where first level list is numRows
        # & second level list will range 0 - 5
        # 2. now for the numbers
        triangle = []
        for i in range(1, numRows):
            prevRow = triangle[i - 1]
            newRow = []
            newRow.append(1)
            for j in range(1, len(prevRow)):
                newRow.append(prevRow[j-1] + prevRow[j])
            newRow.append(1)
            triangle.append(newRow)
        return triangle


obj = Solution()
print(f'{obj.generate(1)}')
