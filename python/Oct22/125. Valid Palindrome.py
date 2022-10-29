class Solution:
    def isPalindrome(self, s: str, type=0) -> bool:
        if type == 0:
            s_alpha = "".join([x.lower() for x in s if x.isalnum()])
            return s_alpha == s_alpha[::-1]
        else:
            l, r = 0, len(s) - 1
            while l < r:
                if not s[l].isalnum():
                    l += 1
                elif not s[r].isalnum():
                    r -= 1
                else:
                    if s[l].lower() != s[r].lower():
                        return False
                    else:
                        l += 1
                        r -= 1
            return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    assert s.isPalindrome("A man, a plan, a canal: Panama", type=1) is True
    assert s.isPalindrome("race a car") is False
    assert s.isPalindrome("") is True
    assert s.isPalindrome(" ") is True
