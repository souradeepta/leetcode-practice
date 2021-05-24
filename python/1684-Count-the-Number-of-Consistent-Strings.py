from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed = set(allowed)
        if not allowed or not words:
            return result
        for i in range(len(words)):
            x = set(words[i])
            if x.issubset(allowed):
                result += 1
        return result


s = Solution()
assert 2 == s.countConsistentStrings(
    "ab", ["ad", "bd", "aaab", "baa", "badab"])
assert 7 == s.countConsistentStrings(
    "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"])
assert 4 == s.countConsistentStrings(
    "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])
