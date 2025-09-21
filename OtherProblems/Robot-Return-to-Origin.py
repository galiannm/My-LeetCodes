class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
        target = (0,0)
        x = y = 0
        for m in moves:
            dx, dy = direction[m]
            x, y = x+dx, y+dy
        return (x, y) == target