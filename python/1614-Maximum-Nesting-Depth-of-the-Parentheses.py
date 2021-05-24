class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        if not s:
            return result
        open = 0
        for char in s:
            if char == "(":
                open += 1
                result = max(result, open)
            elif char == ")":
                open -= 1
        return result


s = Solution()
assert 3 == s.maxDepth("(1+(2*3)+((8)/4))+1"), "incorrect ans"
assert 1 == s.maxDepth("1+(2*3)/(2-1)"), "incorrect ans"
