# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        # traverse to just before middle point
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # cut off to split LL's
        head2 = slow.next
        slow.next = None
        
        # reverse second half in place
        cur = head2
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        head2 = prev
        
        # re order with first and second half
        cur = head
        cur2 = head2

        while cur2:
            next, next2 = cur.next, cur2.next
            cur.next = cur2
            cur2.next = next
            cur = next
            cur2 = next2
