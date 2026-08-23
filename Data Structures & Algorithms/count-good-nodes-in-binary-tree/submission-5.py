# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_value):
            if node is None:
                return 0

            count = 1 if max_value <= node.val else 0
            max_value = max(max_value, node.val)

            left = dfs(node.left, max_value)
            right = dfs(node.right, max_value)

            return count + left + right
        
        return dfs(root, float("-inf"))
        