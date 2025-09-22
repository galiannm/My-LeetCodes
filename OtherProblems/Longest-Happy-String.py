class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        res = []
        while pq:
            cnt1, ch1 = heapq.heappop(pq)
            if len(res) >= 2 and res[-1] == ch1 and res[-2] == ch1:
                if not pq:
                    break
                cnt2, ch2 = heapq.heappop(pq)
                res.append(ch2)
                cnt2 += 1

                if cnt2 < 0:
                    heapq.heappush(pq, (cnt2, ch2))
                heapq.heappush(pq, (cnt1, ch1))
            else:
                res.append(ch1)
                cnt1 += 1
                if cnt1 < 0:
                    heapq.heappush(pq, (cnt1, ch1))
        
        return "".join(res)