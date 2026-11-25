# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.setrecursionlimit(20000)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            current_sum = 0
            if node is None:
                return (0, None)

            if node == p or node == q:
                current_sum = 1

            left_count, left = dfs(node.left)
            right_count, right = dfs(node.right)

            total_count = current_sum + left_count + right_count
            
            
            if left_count == 2:
                return (left_count, left)
            
            if right_count == 2:
                return (right_count, right)

            if total_count == 2:
                return (total_count, node)

            return (total_count, None)
        _, node = dfs(root)
        return node