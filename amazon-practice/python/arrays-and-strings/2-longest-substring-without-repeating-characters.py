# Longest Substring Without Repeating Characters
# Brute force:: Time: O(n^3), Space: O(min(n,n)) We need O(k) space for checking a substring 
# has no duplicate characters, where k is the size of the Set. The size of the Set is upper bounded 
# by the size of the string n and the size of the charset/alphabet m
# 
# Sliding Window Optimzied:: Time:O(n), Space: O(min(n,m)) 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # check for empty input
        if len(s) == 0:
            return 0

        start = -1
        result = 0
        usedChar = {}
        for i in range(len(s)):
            # if character is found in our map, move the start to that character
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = max(start, usedChar[s[i]])
            else:
                # if not then we then we just calculate the new possible result
                result = max(result, i - start)
                
            # add our new character and its index
            usedChar[s[i]] = i
        return result