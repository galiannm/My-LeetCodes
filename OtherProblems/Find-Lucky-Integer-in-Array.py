import collections
from typing import List 

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)

        max_key = -1
        for (key, val) in freq.items():
            if key == val and key > max_key:
                max_key = key
        
        return max_key

        