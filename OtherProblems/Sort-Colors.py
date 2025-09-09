class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Dutch national flag algo
        low, mid, high = 0, 0, len(nums) - 1

        for i in range(len(nums)):
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1

                