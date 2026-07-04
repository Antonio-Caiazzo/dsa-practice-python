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

        while pre:
            post1 = head.next
            post2 = pre.next
            pre.next = post1
            head.next = pre
            head = post1
            pre = post2
        





        