class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return False
        comp= {
            "}": "{",
            "]": "[",
            ")":"("
        }
        stack = []
        for ch in s:
            if ch not in comp:
                stack.append(ch)
            elif not stack or stack.pop() != comp[ch]:
                return False
        return len(stack) == 0
        pass
    def test(self):
        assert(self.isValid("()")==True)
        assert(self.isValid("()[]{}")==True)
        assert(self.isValid("()[]{})")==False)

s=Solution()
s.test()


