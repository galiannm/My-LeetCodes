# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
    
            is_left_balanced, height_left = dfs(root.left)
            is_right_balanced, height_right = dfs(root.right)

            is_balanced = (is_left_balanced and is_right_balanced) and abs(height_right - height_left) <= 1
            return [is_balanced, 1 + max(height_left, height_right)]

        return dfs(root)[0]