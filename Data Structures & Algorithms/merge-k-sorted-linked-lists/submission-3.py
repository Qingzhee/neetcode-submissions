class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                cur_main = lists[i]

                if i + 1 < len(lists):
                    cur_next = lists[i + 1]
                else:
                    cur_next = None

                dummy = ListNode()
                prev = dummy

                while cur_main and cur_next:
                    if cur_main.val <= cur_next.val:
                        holder = cur_main.next
                        prev.next = cur_main
                        prev = prev.next
                        cur_main = holder
                    else:
                        holder = cur_next.next
                        prev.next = cur_next
                        prev = prev.next
                        cur_next = holder

                if cur_main:
                    prev.next = cur_main

                if cur_next:
                    prev.next = cur_next

                merged.append(dummy.next)

            lists = merged

        return lists[0]