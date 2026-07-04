# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        pre = slow.next = None
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        curr = head
        while pre:
            post1 = curr.next
            post2 = pre.next
            pre.next = post1
            curr.next = pre
            curr = post1
            pre = post2
        





        