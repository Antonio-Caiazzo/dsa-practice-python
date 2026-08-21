# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return [True, 0]
            
            left, hl = dfs(node.left)
            right, hr = dfs(node.right)

            return [True if left is True and right and abs(hl - hr) <= 1 else False, 1 + max(hl, hr)]

        result, _ = dfs(root)
        return result
        