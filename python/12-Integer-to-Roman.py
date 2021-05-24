class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        result = ''
        while num > 0:
            for key, value in roman.items():
                if key <= num:
                    result += value
                    num -= key
                    break
        return result


s = Solution()
assert "III" == s.intToRoman(3), "The output is incorrect"
assert "V" == s.intToRoman(5), "The output is incorrect"
assert "MCMXCIV" == s.intToRoman(1994), "The output is incorrect"
assert "LVIII" == s.intToRoman(58), "The output is incorrect"
