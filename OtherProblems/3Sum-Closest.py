class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = nums[l] + nums[i] + nums[r]
                if threeSum == target:
                    return target
                    l+=1
                    while nums[l-1] == nums[l] and l < r: 
                        l+=1
                elif threeSum < target:
                    if abs(target - threeSum) < abs(target - res):
                        res = threeSum
                    l += 1
                else:
                    if abs(target - threeSum) < abs(target - res):
                        res = threeSum
                    r -= 1
        return res