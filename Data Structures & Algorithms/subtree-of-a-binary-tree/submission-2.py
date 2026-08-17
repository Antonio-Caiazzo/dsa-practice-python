# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(node, sub_node):
            if node is None and sub_node is None:
                return True
            if node is None or sub_node is None:
                return False        
            if node.val != sub_node.val:
                return False

            return (is_same_tree(node.left, sub_node.left)
            and
            is_same_tree(node.right, sub_node.right))
     
        def dfs(node):   
            if subRoot is None:
                return True
            if node is None:
                return False

            if is_same_tree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)
        
        