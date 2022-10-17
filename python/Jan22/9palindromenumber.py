class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s == s[::-1] else False
    def test(self):
        assert(self.isPalindrome(121) ==True)
        assert(self.isPalindrome(-121) ==False)

s=Solution()
s.test()