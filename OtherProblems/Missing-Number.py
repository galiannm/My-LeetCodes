class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        total = 0
        for i in range(len(nums)+1):
            total += i
        return total - s