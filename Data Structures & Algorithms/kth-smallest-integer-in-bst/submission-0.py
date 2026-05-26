# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def _inorder(root, output):
            if not root:
                return 
            _inorder(root.left, output)
            output.append(root.val)
            _inorder(root.right, output)
        
        output = []
        _inorder(root, output)

        return output[k-1]