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
            while curr and curr.left:
                curr = curr.left
            return curr.val

        if root is None:
            return

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            minimum = search_min(root.right)
            root.val = minimum
            root.right = self.deleteNode(root.right, minimum)
        return root