class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        max_curr = max_total = nums[0]
        min_curr = min_total = nums[0]

        for n in nums[1:]:
            max_curr = max(n, n + max_curr)
            max_total = max(max_curr, max_total)

            min_curr = min(n, n + min_curr)
            min_total = min(min_curr, min_total)
        
        if max_total < 0:
            return max_total
        
        return max(max_total, total-min_total)



