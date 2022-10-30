class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, slow, fast = 0, 0, 0
        length = 0
        count = {}
        while fast < len(s):
            if s[fast] not in count:
                count[s[fast]] = fast
            else:
                start = max(slow, count[s[fast]] + 1)
                count[s[fast]] = fast
                slow = start
            fast += 1
            length = max(length, fast - slow)

        return length


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abba") == 2
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
