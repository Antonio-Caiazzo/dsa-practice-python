# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        arr = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            arr.append(root.val)
            traversal(root.right)
        traversal(root)
        return arr
        '''
        arr = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            arr.append(cur.val)
            cur = cur.right
        return arr
        
