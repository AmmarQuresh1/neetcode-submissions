# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root, subRoot):
        if not root and not subRoot: return True
        
        if not root or not subRoot: return False
        
        if root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot):
            return True
        else:
            return self.sameTree(root.left, subRoot) or self.sameTree(root.right, subRoot)
        
        
