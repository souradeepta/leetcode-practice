class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        result = 0
        if not s:
            return result
        for c in s:
            if c == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                result += 1
        return result
