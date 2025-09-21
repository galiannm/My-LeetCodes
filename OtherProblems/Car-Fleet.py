class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleats = []
        sorted_cars = sorted(zip(position, speed))
        for pos, vel in sorted_cars[::-1]:
            time = (pos-target) / vel
            if not fleats:
                fleats.append(time)
            elif fleats[-1] > time: 
                fleats.append(time)
        return len(fleats)
