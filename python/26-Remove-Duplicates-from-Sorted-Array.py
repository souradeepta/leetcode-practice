class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums < 2:
            return None
        s, f = 0, 1
        while s < f:
            if nums[s] != nums[f]:
                s+=1
                f+=1
            else:
                nums[s]