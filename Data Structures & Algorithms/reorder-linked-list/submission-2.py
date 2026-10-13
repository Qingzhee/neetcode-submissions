# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        cur1 = head
        cur2 = head.next 
        while cur2 and cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next.next

        # reverse second half:
        cur11 = cur1.next
        cur1.next = None
        prev = None
        while cur11:
            holder1 = cur11.next
            cur11.next = prev
            prev = cur11
            cur11 = holder1

        # prev is now the head of the reveresed half:


        cur3 = head
        while prev:
            holder2 = cur3.next
            holder3 = prev.next

            cur3.next = prev
            prev.next = holder2

            cur3 = holder2
            prev = holder3

    