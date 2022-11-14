class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        pass


s = Solution()
assert s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
assert s.removeStones([[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]]) == 3
