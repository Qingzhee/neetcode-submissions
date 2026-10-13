class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                main = lists[i]
                cur_next = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge(main, cur_next))

            lists = merged

        return lists[0]

    def merge(self, main, cur_next):
        cur_main = main
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

        prev.next = cur_main if cur_main else cur_next
        return dummy.next