class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # counter = set()
        # for ele in nums:
        #     if ele not in counter:
        #         counter.add(ele)
        #     else:
        #         return True
        # return Falsen
        pass

    def test_containsDuplicate(self):
        assert(self.containsDuplicate([1,2,3,1]) == True)
        assert(self.containsDuplicate([1,2,3,4]) == False)
        assert(self.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True)

s = Solution()
s.test_containsDuplicate()