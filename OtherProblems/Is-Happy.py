class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            x = n
            sum_squared = 0
            while x > 0:
                sum_squared += (x%10)**2
                x //= 10
            if sum_squared in seen:
                return False
            seen.add(sum_squared)
            n = sum_squared
        return True