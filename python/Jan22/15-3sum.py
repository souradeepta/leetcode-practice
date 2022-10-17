from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                # to avoid dup triplets
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[j] + nums[k]
                if s < -nums[i]:
                    j+=1
                elif s > -nums[i]:
                    k-=1
                else:
                    trips.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    # below 2 loops to avoid dup triplets
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
        return trips

        pass
    def test(self):
        assert(self.threeSum( [-1,0,1,2,-1,-4]) ==  [[-1,-1,2],[-1,0,1]])
        assert(self.threeSum( []) ==  [])
        assert(self.threeSum( [0]) ==  [])

s=Solution()
s.test()