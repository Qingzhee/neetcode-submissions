# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        book = {}
        cur = head
        while cur is not None:
            if cur not in book:
                book[cur] = 1
            else:
                return True
            cur = cur.next
        return False