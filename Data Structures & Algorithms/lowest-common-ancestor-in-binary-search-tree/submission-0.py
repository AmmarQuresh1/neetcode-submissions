# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findNode(self, root, p, q):
        if not root:
            return False
        
        if root.val == p.val or root.val == q.val:
            return True
        
        return self.findNode(root.left, p, q) or self.findNode(root.right, p, q)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root

        left, right = False, False
        if self.findNode(root.left, p, q):
            left = True
        if self.findNode(root.right, p, q):
            right = True
        
        if left and right:
            return root
        
        if left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif right:
            return self.lowestCommonAncestor(root.right, p, q)