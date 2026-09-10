# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def search_min(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr

        if root is None:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                minimum = search_min(root.right)
                root.val = minimum.val
                root.right = self.deleteNode(root.right, minimum.val)

        return root
        



