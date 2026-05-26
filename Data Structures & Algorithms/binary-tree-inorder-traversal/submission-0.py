# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def _dfs_inorder(root, output):
            if not root:
                return 
            _dfs_inorder(root.left, output)
            output.append(root.val)
            _dfs_inorder(root.right, output)
        
        output = []
        _dfs_inorder(root, output)

        return output