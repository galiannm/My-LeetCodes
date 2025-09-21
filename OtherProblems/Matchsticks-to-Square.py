class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # create 4 groups of equal size
        s = sum(matchsticks)
        if s % 4 != 0: return False
        matchsticks.sort(reverse=True)  
        side_len = s // 4
        side = [0]*4

        def backtrack(i):
            if i >= len(matchsticks): 
                return all(side[i] == side_len for i in range(4))

            for j in range(4):
                if side[j] + matchsticks[i] <= side_len:
                    side[j] += matchsticks[i]
                    if backtrack(i+1): return True
                    side[j] -= matchsticks[i]
                    if side[j] == 0: return False
            return False

        return backtrack(0)
            