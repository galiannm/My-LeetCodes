class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        banned_set = {w.lower() for w in banned}
        words = re.findall(r"[a-z]+", paragraph.lower())
        mp = {}
        for w in words:
            if w not in banned_set:
                mp[w] = mp.get(w, 0) + 1
        return max(mp, key=mp.get)


