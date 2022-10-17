class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 1:
            sign = -1
            x = abs(x)
        result = 0
        while x:
            quotient, remainder = divmod(x, 10)
            result = remainder + result * 10
            x = quotient

            print(result)
        return 0 if result > pow(2, 31) else result * sign

    def test_reverse(self):
        assert self.reverse(123) == 321
        assert self.reverse(-123) == -321


s = Solution()
s.test_reverse()
