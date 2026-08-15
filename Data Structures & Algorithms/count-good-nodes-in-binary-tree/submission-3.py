# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        total = 0

        def dfs(node, max_so_far):
            nonlocal total
            
            if node is None:
                return

            total += 1 if node.val >= max_so_far else 0

            max_so_far = max(max_so_far, node.val)

            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)

        dfs(root, float("-inf"))
        return total
        