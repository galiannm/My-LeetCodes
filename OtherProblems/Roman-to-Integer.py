class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = mp[s[0]]
        for i in range(1, len(s)):
            prev = s[i-1]
            c = s[i]
            if (prev == 'I' and (c == 'V' or c == 'X') or
                prev == 'X' and (c == 'L' or c == 'C') or
                prev == 'C' and (c == 'D' or c == 'M')) :
                res -= mp[prev]
                res += mp[c]-mp[prev]
            else:
                res += mp[c]
        return res