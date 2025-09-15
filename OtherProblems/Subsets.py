class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, subset, i):
            if (i >= len(nums)):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(nums, subset, i+1)
            subset.pop()
            backtrack(nums, subset, i+1)
        backtrack(nums, [], 0)
        return res
