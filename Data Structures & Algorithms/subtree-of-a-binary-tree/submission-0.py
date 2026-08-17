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
            left = is_same_tree(node.left, sub_node.left)
            right = is_same_tree(node.right, sub_node.right)

            return node.val == sub_node.val and left and right
    
        def dfs(node, sub_node):
            if node is None and sub_node is None:
                return True        
            if sub_node is None:
                return True
            if node is None:
                return False
            if is_same_tree(node, sub_node):
                return True
            else:
                left_tree = dfs(node.left, sub_node)
                right_tree = dfs(node.right, sub_node)

            return left_tree or right_tree
            
        return dfs(root, subRoot)
        
        