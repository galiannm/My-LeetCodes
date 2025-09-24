class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1
        
        res_start, res_end = 0, 0
        for i in range(n):
            # odd middle check
            l, r = expand(i, i)
            if r-l > res_end-res_start:
                res_end, res_start = r, l 

            # even middle check
            l, r = expand(i, i+1)
            if r-l > res_end-res_start:
                res_end, res_start = r, l  

        return s[res_start:res_end+1]


