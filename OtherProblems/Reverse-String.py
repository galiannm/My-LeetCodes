class Solution:
    def reverseString(self, s: List[str]) -> None:
        r = len(s)-1
        l = 0
        while (r > l):
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1 