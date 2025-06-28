import heapq
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        heapq.heapify(arr)
        for i in range(len(nums)):
            heapq.heappush(arr,[nums[i],i])
            if len(arr) > k:
                heapq.heappop(arr)
        def f(x):
            return x[1]
        arr = sorted(arr, key = f)
        res = []
        for i in range(len(arr)):
            res.append(arr[i][0])
        return res
