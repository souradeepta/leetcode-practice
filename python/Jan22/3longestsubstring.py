class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = {}
        left, right = 0, 0
        longest = 1
        while right <len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]]+1)
            longest = max(longest, right - left + 1)

            seen[s[right]] = right
            right +=1

        return longest

    def test_lengthOfLongestSubstring(self):
        assert(self.lengthOfLongestSubstring("abcabcbb") ==3)
        assert(self.lengthOfLongestSubstring("pwwkew") ==3)
        assert(self.lengthOfLongestSubstring("bbbbb") ==1)

s = Solution()

s.test_lengthOfLongestSubstring()
