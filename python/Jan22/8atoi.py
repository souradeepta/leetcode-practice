import re

class Solution:
    def myAtoi(self, str):
        # write your code here
        intMax = 2147483647
        intMin = -2147483648
        str = str.strip()
        if not str:
            return 0
        sign, i = 1, 0
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        num = 0
        while i < len(str):
            if not str[i].isdigit():
                break
            num = num * 10 + ord(str[i]) - ord('0')
            if num > intMax:
                break
            i += 1
        return min(max(sign * num, intMin), intMax)
    def test_myAtoi(self):
        assert(self.myAtoi("42")==42)
        assert(self.myAtoi("      -42")==-42)
        assert(self.myAtoi("4193 with words")==4193)

s=Solution()
s.test_myAtoi()