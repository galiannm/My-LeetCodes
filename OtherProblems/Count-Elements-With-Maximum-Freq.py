class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0] * 101
        maxFreq = 0
        res = 0
        for n in nums:
            freq[n] += 1
            f = freq[n]
            if f > maxFreq:
                maxFreq = f
                res = f
            elif f == maxFreq:
                res += f
        return res

        
        