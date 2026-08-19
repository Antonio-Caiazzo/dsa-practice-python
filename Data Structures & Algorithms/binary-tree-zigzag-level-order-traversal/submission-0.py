# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        if root is None:
            return result
        
        queue = deque([root])

        level = 0
        while queue:
            level_size = len(queue)
            level_list = []

            for _ in range(level_size):

                node = queue.popleft()

                level_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 0:
                result.append(level_list)
            else:
                level_list.reverse()
                result.append(level_list)
            
            level += 1
        
        return result




        