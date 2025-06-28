from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r, l, i = m+n-1, m-1, n-1
        while i >= 0: 
            if l >= 0 and nums1[l] > nums2[i]:
                nums1[r] = nums1[l]
                l -= 1
            else:
                nums1[r] = nums2[i]
                i -= 1
            r -= 1




        