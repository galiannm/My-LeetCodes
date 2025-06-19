from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        setNums = set(nums)
        for num in nums:
            if (num - 1) not in setNums:
                length = 1
                while (num+length) in setNums:
                    length += 1
                res = max(res, length)
        return res
