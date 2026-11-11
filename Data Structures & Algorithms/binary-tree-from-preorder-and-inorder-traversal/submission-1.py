# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        positions = {value: i for i, value in enumerate(inorder)}
        pre_index = 0

        def dfs(left, right):
            if left > right:
                return None
            
            nonlocal pre_index
            root_value = preorder[pre_index]
            pre_index += 1

            root = TreeNode(root_value)
            
            mid = positions[root_value]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)