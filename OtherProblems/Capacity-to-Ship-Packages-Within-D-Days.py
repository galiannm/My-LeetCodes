class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canPartition(cap):
            daysUsed = 1
            curr = 0
            for w in weights:
                if w > cap:
                    return False
                if curr + w > cap:
                    daysUsed += 1
                    curr = 0
                curr += w
            return daysUsed <= days

        res = 0
        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if canPartition(mid):
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1
        return res
