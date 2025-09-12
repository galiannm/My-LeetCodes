class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS solution
        m, n = len(grid), len(grid[0])

        def DFS(x, y):
            if (x not in range(m) or y not in range(n) 
            or grid[x][y] != '1'):
                return
            grid[x][y] = '0'
            DFS(x+1, y)
            DFS(x-1, y)
            DFS(x, y+1)
            DFS(x, y-1)

        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    DFS(x, y)
                    res += 1
        return res