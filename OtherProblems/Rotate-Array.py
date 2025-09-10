class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        start = count = 0

        while count < n:
            current = start 
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                prev, nums[next_idx] = nums[next_idx], prev
                current = next_idx
                count += 1
                if current == start:
                    break
            start += 1