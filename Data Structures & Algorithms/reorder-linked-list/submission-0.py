# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head 
        size = 0
        # get size of LL
        while cur:
            cur = cur.next 
            size += 1
        
        # traverse to just before middle point
        cur = head
        for _ in range(int(size/2) - 1):
            cur = cur.next 
        
        # cut off to split LL's
        head2 = cur.next
        cur.next = None
        
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

        while cur.next and cur2.next:
            next, next2 = cur.next, cur2.next
            cur.next = cur2
            cur = next
            cur2.next = cur
            cur2 = next2
        
        if cur:
            cur.next = cur
        if cur2:
            cur.next = cur2
