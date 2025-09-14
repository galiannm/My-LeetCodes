class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        v = set()

        def DFS(x, y):
            if x not in range(n) or y not in range(m): return 1
            if grid[x][y] == 0: return 1
            if ((x,y) in v): return 0
            v.add((x,y))

            return DFS(x+1, y) + DFS(x-1, y) + DFS(x, y+1) + DFS(x, y-1)

        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 1):
                    return DFS(i, j)

        return 0
        

