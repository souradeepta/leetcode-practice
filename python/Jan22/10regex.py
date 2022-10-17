class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
    def test(self):
        assert(self.isMatch("aa", "a")==False)
        assert(self.isMatch("aa", "a*")==True)
        assert(self.isMatch("ab", ".*")==True)

s=Solution()
s.test()