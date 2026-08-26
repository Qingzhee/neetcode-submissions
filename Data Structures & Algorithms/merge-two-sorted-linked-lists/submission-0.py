# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
    
        dummy = ListNode()
        prev = dummy
        
        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                prev.next = cur1
                cur1 = cur1.next
            else:
                prev.next = cur2
                cur2 = cur2.next
            prev = prev.next

        while cur1 is not None:
            prev.next = cur1
            cur1 = cur1.next
            prev = prev.next

        while cur2 is not None:
            prev.next = cur2
            cur2 = cur2.next
            prev = prev.next
            
        return dummy.next