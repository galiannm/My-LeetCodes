# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val > key: # left
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: # right 
            root.right = self.deleteNode(root.right, key)
        else: # found node to delete
            if not root.left: return root.right
            if not root.right: return root.left

            succ = self.min(root.right)
            root.val = succ.val
            root.right = self.deleteMin(root.right)

        return root
    
    def deleteMin(self, root):
        if not root.left: return root.right
        root.left = self.deleteMin(root.left)
        return root

    def min(self, root):
        if not root.left: return root
        return self.min(root.left)
