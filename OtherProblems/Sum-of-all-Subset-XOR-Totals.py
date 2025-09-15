class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.backtrack(nums, 0, nums[0])
    
    def backtrack(self, nums, i, curr):
        if i == len(nums): return curr
        return self.backtrack(nums, i+1, curr) + self.backtrack(nums, i+1, curr^nums[i])