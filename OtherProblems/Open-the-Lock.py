class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        dead = set(deadends)

        if start in dead:
            return -1
        if target == start:
            return 0

        def neighbors(code: str):
            for i in range(4):
                d = int(code[i])
                # turn up
                up = (d + 1) % 10
                yield code[:i] + str(up) + code[i+1:]
                # turn down
                down = (d - 1) % 10
                yield code[:i] + str(down) + code[i+1:]
        
        seen = {start}
        q = deque([(start, 0)])

        while q: 
            curr, moves = q.popleft()
            for nxt in neighbors(curr):
                if nxt not in dead and nxt not in seen:
                    if nxt == target:
                        return moves+1
                    seen.add(nxt)
                    q.append((nxt, moves+1))
        
        return -1