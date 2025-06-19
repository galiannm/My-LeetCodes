from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area = min(h1, h2) * idx(h2)-idx(h1)
        l, r = 0, len(height)-1
        res = 0
        while l <= r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res   