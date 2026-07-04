# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        elif head.next is None and n == 1:
            return None
        else:
            dummy = ListNode(0, head)
            left = dummy
            right = head

            while right and n:
                right = right.next
                n -= 1

            while right:

                right = right.next
                left = left.next
    
            left.next = left.next.next

        return dummy.next
        
        