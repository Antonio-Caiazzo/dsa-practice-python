"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        oldToNew = {node: Node(node.val)}
        queue = deque([node])

        while queue:
                vertex = queue.popleft()

                for neighbor in vertex.neighbors:

                    if neighbor not in oldToNew:
                        copy = Node(neighbor.val)
                        oldToNew[neighbor] = copy
                        queue.append(neighbor)

                    oldToNew[vertex].neighbors.append(oldToNew[neighbor])
 
        return oldToNew[node]
        