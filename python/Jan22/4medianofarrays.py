from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if (len1 + len2)%2 !=0:
            return self.get_kth(nums1, nums2,0, len1-1, 0, len2-1, (len1+len2)//2)
        else:
            mid1 = self.get_kth(nums1, nums2,0, len1-1, 0, len2-1, (len1+len2)//2)
            mid2 = self.get_kth(nums1, nums2,0, len1-1, 0, len2-1, (len1+len2)//2 -1)
            return (mid1+mid2)/2

    def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
        if start1 > end1:
            return nums2[k-start1]
        if start2 > end2:
            return nums1[k-start2]

        mid1 = (start1+end1)//2
        mid2=(start2+end2)//2
        mid1_val = nums1[mid1]
        mid2_val = nums2[mid2]

        if (mid1+mid2) < k:
            if mid1_val > mid2_val:
                return self.get_kth(nums1, nums2, start1, end1, mid2+1, end2, k)
            else:
                return self.get_kth(nums1, nums2, mid1+1, end1, start1, end2, k)
        else:
            if mid1_val > mid2_val:
                return self.get_kth(nums1, nums2, start1, mid1-1, start2, end2, k)
            else:
                return self.get_kth(nums1, nums2, start1, end1, start2, mid2-1, k)

    def test_findMedianSortedArrays(self):
        assert self.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
        assert self.findMedianSortedArrays([1, 3], [2]) == 2.0


s = Solution()

s.test_findMedianSortedArrays()
