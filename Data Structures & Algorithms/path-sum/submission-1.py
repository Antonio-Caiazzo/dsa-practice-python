# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node):
            nonlocal targetSum
            if node is None:
                return False
            targetSum -= node.val
            if node.left is None and node.right is None and targetSum == 0:
                return True

            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            targetSum += node.val
        
            return False


        return dfs(root)
        