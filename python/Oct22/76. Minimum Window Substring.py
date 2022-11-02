from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str, type=0) -> str:
        """Given two strings s and t of lengths m and n
        respectively, return the minimum window substring
        of s such that every character in t (including
        duplicates) is included in the window. If there is
        no such substring, return the empty string "".

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            str: _description_
        """
        if type == 0:
            if t == "":
                return ""

            countT, window = {}, {}
            for c in t:
                countT[c] = 1 + countT.get(c, 0)

            have, need = 0, len(countT)
            res, resLen = [-1, -1], float("infinity")
            l = 0
            for r in range(len(s)):
                c = s[r]
                window[c] = 1 + window.get(c, 0)

                if c in countT and window[c] == countT[c]:
                    have += 1

                while have == need:
                    # update our result
                    if (r - l + 1) < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    # pop from the left of our window
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
            l, r = res
            return s[l : r + 1] if resLen != float("infinity") else ""
        if type == 1:
            # sliding
            if not t or not s:
                return ""
            len_s, len_t = len(s), len(t)

            # ans tuple of the form (window length, left, right)
            min_win_sub = float("inf"), None, None
            matched_digits = 0
            count_t = Counter(t)
            required_unique = len(count_t)
            left, right = 0, 0

            curr_reg = {}
            while right < len_s:
                char = s[right]
                curr_reg[char] = curr_reg.get(char, 0) + 1

                if char in count_t and curr_reg[char] == count_t[char]:
                    matched_digits += 1

                while left <= right and matched_digits == required_unique:
                    char = s[left]

                    if right - left + 1 < min_win_sub[0]:
                        min_win_sub = (right - left, left, right)

                    curr_reg[char] -= 1
                    if char in count_t and curr_reg[char] < count_t[char]:
                        matched_digits -= 1

                    left += 1

                right += 1

            return (
                ""
                if min_win_sub[0] == float("inf")
                else s[min_win_sub[1] : min_win_sub[2] + 1]
            )

        elif type == 2:
            # not working brute force
            len_s, len_t = len(s), len(t)
            min_win_sub = []
            matched_digits = 0
            for i in range(len_s):
                count_t = Counter(t)
                curr_win_sub = []
                for j in range(i, len_s):
                    # found char in s and t
                    if s[j] in count_t:
                        count_t[s[j]] -= 1
                        curr_win_sub.append(s[j])
                    # found invalid char in window
                    elif s[j] not in count_t and curr_win_sub:
                        curr_win_sub.append(s[j])
                    # one completed match for t in s
                    if s[j] in count_t and count_t[s[j]] == 0:
                        matched_digits += 1
                    # all in t matched to s
                    if matched_digits == len(count_t):
                        break
                print(curr_win_sub)
                min_win_sub = (
                    curr_win_sub
                    if len(curr_win_sub) > len(min_win_sub)
                    else min_win_sub
                )
            print(min_win_sub)
            return "".join(min_win_sub)

        pass


if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "t") == "a"
    assert s.minWindow("a", "aa") == ""
    assert s.minWindow("a", "") == ""
