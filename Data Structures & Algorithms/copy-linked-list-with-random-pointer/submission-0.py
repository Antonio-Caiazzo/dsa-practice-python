"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        random_point = {}
        while curr:
            new_copy = Node(curr.val)
            random_point[curr] = new_copy
            
            curr = curr.next

        new_head = random_point[head]
        new_curr = new_head

        while head:
            new_curr = random_point[head]
            new_curr.next = random_point.get(head.next)
            new_curr.random = random_point.get(head.random)

            head = head.next
            
        return new_head

