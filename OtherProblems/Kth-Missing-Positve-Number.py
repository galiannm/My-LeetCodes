class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        lo, hi = 0, n-1

        def count_missing(x):
            return arr[x] - (x+1)

        while lo <= hi:
            mid = (lo+hi)//2
            if count_missing(mid) < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return arr[hi] + k - count_missing(hi)
