class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        stri = str(n)
        p, s = 1, 0

        for i in stri:
            p *= ord(i)-ord('0')
            s += ord(i)-ord('0')
        return p-s


s = Solution()
assert 15 == s.subtractProductAndSum(234), "incorrect solution"
assert 21 == s.subtractProductAndSum(4421), "incorrect solution"
