# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = deque([target])
        visited = set([target])
        parent = {}

        def dfs(node, par=None):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        res = []
        while q and k > 0: 
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                neighbor = [parent[node], node.left, node.right]
                for nei in neighbor:
                    if nei and nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            k -= 1

        return [node.val for node in q]