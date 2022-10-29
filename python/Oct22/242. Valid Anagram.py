from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str, type=0) -> bool:
        """compare if 2 strings are anagrams

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        Complexity:
            Time O(s+t)
            Space O(s+t)
            second one is Time O(nlogn), Space O(1)
        """
        if type == 0:
            return Counter(s) == Counter(t)
        else:
            # neetcode
            return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "cat") is False
    assert s.isAnagram("cat", "bat") is False
    assert s.isAnagram("", "bat") is False
    assert s.isAnagram("anagram", "nagaram", type=1) is True
