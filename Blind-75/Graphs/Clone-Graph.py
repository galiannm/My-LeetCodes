"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        old_to_new = { node: Node(node.val) }
        def dfs(u):
            clone_u = old_to_new[u]
            for v in u.neighbors:
                if v not in old_to_new:
                    old_to_new[v] = Node(v.val)
                    dfs(v)
                clone_u.neighbors.append(old_to_new[v])
        dfs(node)
        return old_to_new[node]
