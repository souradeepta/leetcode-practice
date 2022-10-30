class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        freq = {}
        maxlen = 0
        for r in range(len(s)):
            # If a character is not in the frequency dict, this inserts it with a value of 1 (get returns 0, then we add 1).
            # If a character is in the dict, we simply add one.
            freq[s[r]] = freq.get(s[r], 0) + 1

            # The key point is that we only care about the MAXIMUM of the seen values.
            # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
            cur_len = r - l + 1

            # if we have replaced <= K letters, record a new maxLen
            if cur_len - max(freq.values()) <= k:
                maxlen = max(maxlen, cur_len)
            else:
                # if we have replaced > K letters, then it's time to slide the window
                # decrement frequency of char at left pointer, then increment pointer
                freq[s[l]] -= 1
                l += 1

        return maxlen


if __name__ == "__main__":
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
    assert s.characterReplacement("", 2) == 0
    assert s.characterReplacement("A", 2) == 1
    assert s.characterReplacement("AAAAAAAAAA", 2) == 10
    # assert s.characterReplacement("ABCDEFGH", 2) == 3
    assert s.characterReplacement("ASDFD", 0) == 1
