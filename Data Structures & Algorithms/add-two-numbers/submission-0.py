# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur, cur2, cur3 = l1, l2, dummy

        carry = 0
        while cur and cur2:
            val = (cur.val + cur2.val + carry) % 10
            carry = (cur.val + cur2.val + carry) // 10

            cur3.next = ListNode(val)

            cur, cur2, cur3 = cur.next, cur2.next, cur3.next

        while cur:
            val = (cur.val + carry) % 10
            carry = (cur.val + carry) // 10

            cur3.next = ListNode(val)

            cur, cur3 = cur.next

        while cur2:
            val = (cur2.val + carry) % 10
            carry = (cur2.val + carry) // 10

            cur3.next = ListNode(val)
            cur2, cur3 = cur2.next, cur3.next

        if carry > 0:
            cur3.next = ListNode(carry)
            cur3 = cur3.next
        
        return dummy.next
