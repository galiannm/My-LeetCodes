class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        res = set()
        for n in nums2:
            if n in set1:
                res.add(n)
        return list(res)