from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r, m_l, n_l = m+n-1, m-1, n-1
        while n_l >= 0: 
            if m_l >= 0 and nums1[m_l] > nums2[n_l]:
                nums1[r] = nums1[m_l]
                m_l -= 1
            else:
                nums1[r] = nums2[n_l]
                n_l -= 1
            r -= 1




        