# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(cur, sum = 0):
            # at leaf check if = targetSum
            sum += cur.val
            if not cur.left and not cur.right:
                return sum == targetSum
            
            if cur.left and dfs(cur.left, sum): return True
            if cur.right and dfs(cur.right, sum): return True

            return False
        
        return dfs(root)
