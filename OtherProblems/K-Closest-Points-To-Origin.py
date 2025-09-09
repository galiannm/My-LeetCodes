class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = sqrt(x**2 + y**2)
            heapq.heappush(h, (-dist, (x, y)))
            if (len(h) > k):
                min_elem = heapq.heappop(h)
        
        res = [h[i][1] for i in range(len(h))]
        return res
        