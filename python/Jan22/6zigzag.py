class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = [""]*numRows
        row_idx = 1
        going_up = True

        for ch in s:
            result[row_idx-1] +=ch
            if row_idx == numRows:
                going_up = False
            elif row_idx == 1:
                going_up = True

            if going_up:
                row_idx +=1
            else:
                row_idx -=1

        return "".join(result)

    def test_convert(self):
        assert(self.convert("PAYPALISHIRING", 3)=="PAHNAPLSIIGYIR")
        assert(self.convert("PAYPALISHIRING", 4)=="PINALSIGYAHRPI")

s = Solution()
s.test_convert()