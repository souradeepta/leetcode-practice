class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: return ''
        mini, maxi = min(strs), max(strs)
        for i, letter in enumerate(mini):
            if letter!=maxi[i]:
                return mini[:i]
        print(mini)
        return mini
    def test(self):
        assert(self.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")


s=Solution()
s.test()