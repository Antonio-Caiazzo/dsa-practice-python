# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_subRoot(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False
            
            if root.val != subRoot.val:
                return False

            return is_subRoot(root.left, subRoot.left) and is_subRoot(root.right, subRoot.right)

        def dfs(node):
            if node is None and subRoot is None:
                return True
            elif node is None or subRoot is None:
                return False

            if node.val == subRoot.val and is_subRoot(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)


        return dfs(root)
        