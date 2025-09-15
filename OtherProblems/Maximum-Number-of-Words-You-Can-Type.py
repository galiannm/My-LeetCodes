class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        bls = set(brokenLetters)
        res = len(words)
        for w in words:
            for c in w:
                if c in bls: 
                    res -= 1
                    break
        return res