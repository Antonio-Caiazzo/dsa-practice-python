# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, depth):
            if root is None:
                return (0, True)

            depth = depth + 1
            left, check_left = dfs(root.left, depth)
            right, check_right = dfs(root.right, depth)
            

            return (1 + max(left, right), (abs(left - right) <= 1) and check_left and check_right)
        _, result = dfs(root, 0)

        return result