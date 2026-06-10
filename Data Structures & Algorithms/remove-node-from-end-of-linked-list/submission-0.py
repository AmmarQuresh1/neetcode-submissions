# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy_head = ListNode(0, head)

        slow, fast = dummy_head.next, dummy_head.next

        counter = 0
        while fast.next:
            if counter >= n:
                slow = slow.next
            fast = fast.next

            counter += 1

        # remove the node 
        if fast and slow.val == fast.val:
            return None
        
        slow.next = fast
        return dummy_head.next
