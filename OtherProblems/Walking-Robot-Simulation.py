class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        x = y = 0
        res = 0
        obst = set(map(tuple, obstacles))
        for c in commands:
            if c == -1: d = (d+1)%4
            elif c == -2: d = (d-1)%4
            else:
                dx, dy = directions[d]
                for _ in range(c):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obst:
                        break
                    x, y = nx, ny
                    res = max(res, x*x + y*y)
        return res
