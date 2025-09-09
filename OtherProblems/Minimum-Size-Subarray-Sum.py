class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        res = len(nums) + 1
        for r in range(len(nums)):
            sum += nums[r]
            if sum >= target:
                while sum - nums[l] >= target:
                    sum -= nums[l]
                    l += 1 
                res = min(res, r - l + 1)
        if res == len(nums) + 1:
            return 0
        else:
            return min(res, r - l + 1)
            