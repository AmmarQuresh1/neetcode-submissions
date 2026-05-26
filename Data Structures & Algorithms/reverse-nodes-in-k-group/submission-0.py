# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                if kth:
                    kth = kth.next

            if not kth:
                break

            # reverse in place
            group_next = kth.next

            prev = group_next 
            cur = group_prev.next
            while cur != group_next:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            group_tail = group_prev.next
            group_prev.next = kth
            group_prev = group_tail
        
        return dummy.next
