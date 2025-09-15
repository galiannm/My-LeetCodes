class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        flip = -1
        res = count = 1
        for r in range(1, len(arr)):
            if arr[r-1] < arr[r] and (flip == 0 or flip == -1):
                count += 1
                flip = 1
            elif arr[r] < arr[r-1] and (flip == 1 or flip == -1):
                count += 1
                flip = 0
            else: 
                if arr[r] == arr[r-1]:
                    flip = -1
                    count = 1
                else:
                    count = 2
                    flip = 1 if arr[r-1] < arr[r] else 0
            res = max(count, res)
        return res
