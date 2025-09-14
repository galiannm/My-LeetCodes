class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l1, l2 = len(word1), len(word2)
        for i in range(max(l1, l2)):
            if i in range(l1):
                res.append(word1[i])
            if i in range(l2):
                res.append(word2[i])
        return "".join(res)
