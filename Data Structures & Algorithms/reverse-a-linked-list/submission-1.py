# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 1 2 3
        #     p c 
        # 1st: 0 points to none, next = 1, cur = next, prev = 0
        # 2nd: 1 points to 0, next = 2, cur = 2, prev = 1
        # 3rd: 2 points to 1, next = 3, prev = 2, cur = 3
        # 4th: next = None, 3 points to 2, prev = 3, cur = next = None
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev