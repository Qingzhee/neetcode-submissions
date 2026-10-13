# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counts = 0
        cur = head
        while cur:
            counts+=1
            cur = cur.next
        new = counts-n
        if new == 0:  
            return head.next

        cur_idx = 0
        cur = head
        prev = None
        holder = None
        while cur_idx != new:
            prev = cur
            cur = cur.next
            cur_idx+=1
            holder = cur.next
        prev.next = holder
        return head



        
