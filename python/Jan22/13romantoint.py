class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D": 500,
            "M":1000
        }
        result = 0
        prev = 0
        for ch in s[::-1]:
            if ref[ch] >= prev:
                result += ref[ch]
            else:
                result -= ref[ch]
            prev = ref[ch]

        return result


    def test(self):
        assert(self.romanToInt("III")==3)
        assert(self.romanToInt("LVIII")==58)


s=Solution()
s.test()