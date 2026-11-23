# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if node is None or node.next is None:
                return node
            second, first = node, node.next
            succ = second.next.next
            first.next = second
            second.next = helper(succ)
            
            return first
        return helper(head)