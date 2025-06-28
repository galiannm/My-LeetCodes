class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        lo, hi = 1, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                hi = mid-1
            else:
                lo = mid+1
        return hi