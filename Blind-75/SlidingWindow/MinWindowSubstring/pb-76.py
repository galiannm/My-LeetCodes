class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return "" 
        window, countT = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        need, have = len(countT), 0
        res, minLength = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1) < minLength:
                    res = [l,r]
                    minLength = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if (minLength != float('inf')) else ""
