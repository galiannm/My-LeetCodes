class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def DFS(x, y, v):
            v.add((x, y))
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny = x + dx, y + dy
                if (nx in range(m) and ny in range(n) and
                (nx, ny) not in v and
                heights[nx][ny] >= heights[x][y]):
                    DFS(nx, ny, v)
        
        for r in range(m):
            DFS(r, 0, pac)
            DFS(r, n-1, atl)

        for c in range(n):
            DFS(0, c, pac)
            DFS(m-1, c, atl)

        return [[x, y] for x in range(m) for y in range(n) if (x, y) in pac and (x, y) in atl]