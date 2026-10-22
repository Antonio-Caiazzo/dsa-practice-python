# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        count = 0
        while curr or stack:
            
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                count += 1
                if k == count and node:
                    return node.val
                curr = node.right
            
            



