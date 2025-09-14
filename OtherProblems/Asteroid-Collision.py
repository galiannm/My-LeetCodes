class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # abs value -> size
        # sign (-, +) -> direction (left, right)
        # same speed for all 

        # same size (both explode) | smaller explodes
        # same direction -> never collide

        def collide(a, b):
            return b > 0 and a < 0

        s = []
        for a in asteroids:
            if not s:
                s.append(a)
            else: 
                alive = True
                while s and alive and collide(a, s[-1]):
                    if abs(s[-1]) < abs(a):
                        s.pop()
                    elif abs(s[-1]) == abs(a):
                        s.pop()
                        alive = False
                    else: alive = False
                if alive: s.append(a)
        return s
                


