class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        result = ""
        for i in d:
            result += (num//i)*d[i]
            num %=i
        return result

    def test(self):
        assert(self.intToRoman(3) == "III")

s =Solution()
s.test()