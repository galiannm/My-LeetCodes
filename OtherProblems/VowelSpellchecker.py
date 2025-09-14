class Solution:
    def deVowel(self, w):
        return "".join('-' if c in 'aeiou' else c for c in w)

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        s = set(wordlist)
        caseMp, vowelMp  = {}, {}

        # get first occurent of lower case word
        for w in wordlist:
            wl = w.lower()
            wd = self.deVowel(wl)
            if wl not in caseMp:
                caseMp[wl] = w
            if wd not in vowelMp:
                vowelMp[wd] = w

        for q in queries:
            wordMatch = ""
            # 1. exact match
            if q in s:
                wordMatch = q
            elif wordMatch == "":
                ql = q.lower()
                # 2. case in-sens
                if ql in caseMp:
                    wordMatch = caseMp[ql]
                # 3. Vowel diff
                elif self.deVowel(ql) in vowelMp:
                    wordMatch = vowelMp[self.deVowel(ql)]
            res.append(wordMatch)
        return res
                    
                
