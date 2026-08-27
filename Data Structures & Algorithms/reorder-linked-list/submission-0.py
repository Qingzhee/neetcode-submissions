# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        counts = 0
        cur = head

        while cur is not None:
            counts += 1
            cur = cur.next

        cur1 = head
        while counts > 2:
            holder = cur1.next
            cur2 = cur1

            for i in range(counts - 1):
                prev = cur2
                cur2 = cur2.next

            cur1.next = cur2
            cur2.next = holder
            prev.next = None

            cur1 = holder
            counts -= 2


