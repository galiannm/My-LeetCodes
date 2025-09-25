class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find first decreasing elem, x, from the right 
        # fin smallest elem greater than x, y
        # swap x and y
        # reverse the sublist from x to end of the list

        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        j = len(nums)-1
        while j > 1 and nums[j] <= nums[i-1]:
            j -= 1

        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
        
        
                
            

        