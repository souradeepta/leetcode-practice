class Solution:
    def trap(self, height: list[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9
