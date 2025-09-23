class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = {} 
        freqs = []
        res = []
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        for ch, cnt in mp.items():
            heapq.heappush(freqs,  (-cnt, ch))

        while freqs:
            cnt1, ch1 = heapq.heappop(freqs)
            if not res or res[-1] != ch1:
                res.append(ch1)
                cnt1 += 1
                if cnt1 != 0:
                    heapq.heappush(freqs,  (cnt1, ch1))
            else: 
                if not freqs: 
                    return "" 
                cnt2, ch2 = heapq.heappop(freqs)
                res.append(ch2)
                cnt2 += 1
                heapq.heappush(freqs,  (cnt1, ch1))
                if cnt2 != 0:
                    heapq.heappush(freqs,  (cnt2, ch2))
        return "".join(res)

        