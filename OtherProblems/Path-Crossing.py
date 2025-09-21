class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {'N':(0,1), 'S':(0,-1), 'E':(1, 0), 'W':(-1,0)}
        x = y = 0
        mp = {(0,0)}
        for d in path:
            dx, dy = direction[d]
            x, y = x + dx, y + dy
            if (x, y) in mp: 
                return True
            mp.add((x, y))
        return False
            