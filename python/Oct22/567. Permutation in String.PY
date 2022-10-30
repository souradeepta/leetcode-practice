from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str, type=0) -> bool:
        """Given two strings s1 and s2, return true
        if s2 contains a permutation of s1, or false otherwise.

        Args:
            s1 (str): _description_
            s2 (str): _description_

        Returns:
            bool: _description_
        Time: O(n) - linear for window sliding and counter
        Space: O(1) - conctant for dictionary
        with the maximum 26 pairs (English alphabet)
        """
        if type == 0:
            count_s1 = Counter(s1)
            match_len = len(s1)
            length_s2 = len(s2)
            for i in range(length_s2):
                if s2[i] in count_s1:
                    count_s1[s2[i]] -= 1
                if i >= match_len and s2[i - match_len] in count_s1:
                    count_s1[s2[i - match_len]] += 1

                # see optimized code in else
                if all([count_s1[i] == 0 for i in count_s1]):
                    return True

                # remove 0 or negative count elements. Wierd bug
                # count_s1 = +count_s1
                # if not len(count_s1):
                #     return True
            return False
        elif type == 1:
            # We can use an auxiliary variable to count a number of
            # characters whose frequency gets to zero during window
            # sliding. That helps us to avoid iterating over the hashmap
            # for every cycle tick to check whether frequencies turned
            # into zero.
            cntr, w, matched = Counter(s1), len(s1), 0

            for i in range(len(s2)):
                if s2[i] in cntr:
                    cntr[s2[i]] -= 1
                    if cntr[s2[i]] == 0:
                        matched += 1
                # I had trouble understanding this too, after breaking it
                # down a bit.
                # I believe i-w at each iteration equals to one index to the
                # left outside our sliding window.
                # We use i-w (w = len(s1)) because it lags behind by the size
                # of the s1.
                # In example: s1 = "ab", s2 = "eidboaoo" | i-w at each
                # iteration in s2 = [-2,-1,0,1,2,3,4,5] => [-,-,e,i,d,b,o,a].
                # Notice that we enter this line at iteration 5 and 7,
                # when we are outside of the current window.
                # The idea is we already passed it and we didn't find
                # all the letters in the hash table, so we should restore
                # the letter back in the table in case our potential substring
                # is further down s2.
                if i >= w and s2[i - w] in cntr:
                    if cntr[s2[i - w]] == 0:
                        matched -= 1
                    cntr[s2[i - w]] += 1

                if matched == len(cntr):
                    return True

            return False
        else:
            n1 = len(s1)
            n2 = len(s2)

            if n1 > n2:
                return False

            s1Count = [0] * 26
            s2Count = [0] * 26

            # initial values for first set of window
            for i in range(n1):
                s1Count[ord(s1[i]) - ord("a")] += 1
                s2Count[ord(s2[i]) - ord("a")] += 1

            for i in range(n2 - n1):  # n2-n1 is the number of slides
                if s1Count == s2Count:
                    return True

                # reduce leaving char count
                s2Count[ord(s2[i]) - ord("a")] -= 1

                # increase introduced char count
                s2Count[ord(s2[i + n1]) - ord("a")] += 1

            return s1Count == s2Count


if __name__ == "__main__":
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") is True
    assert s.checkInclusion("ab", "eidbaooo", type=1) is True
    assert s.checkInclusion("ab", "eidbaooo", type=2) is True
    assert s.checkInclusion("ab", "eidboaooo") is False
    assert s.checkInclusion("ab", "") is False
