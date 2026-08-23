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

            left = dfs(node.left)
            if not left[0]:
                return [False, left[1]]
            
            right = dfs(node.right)

            return [True if left[0] is True and right[0] is True and abs(left[1] - right[1]) <= 1 else False, 1 + max(left[1], right[1])]

        
        return dfs(root)[0]