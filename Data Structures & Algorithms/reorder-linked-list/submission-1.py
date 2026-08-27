# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur1 = head
        cur2 = head
        while cur2 is not None and cur2.next is not None:
            cur1 = cur1.next
            cur2 = cur2.next.next
        
        cur3 = cur1.next
        cur1.next = None

        prev = None
        # reverse the second half:
        while cur3 is not None:
            holder = cur3.next
            cur3.next = prev

            prev = cur3
            cur3 = holder

        cur4 = head
        while prev is not None:
            holder1 = cur4.next
            holder2 = prev.next

            cur4.next = prev
            prev.next = holder1

            cur4 = holder1
            prev = holder2
        