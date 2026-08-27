# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur1 = head
        cur2 = head
        while cur2 is not None and cur2.next is not None:
            cur1 = cur1.next
            cur2 = cur2.next.next
            if cur2 == cur1:
                return True
        return False