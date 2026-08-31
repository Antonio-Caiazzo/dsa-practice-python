# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum_diameter = 0
        def dfs(node):
            if node is None:
                return 0
            
            nonlocal maximum_diameter

            left = dfs(node.left)
            right = dfs(node.right)

            maximum_diameter = max(maximum_diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return maximum_diameter
        