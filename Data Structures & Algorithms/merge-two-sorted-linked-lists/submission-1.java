/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // New empty listnode
        ListNode head = new ListNode();
        ListNode tail = head;
        // Assign current pointers for list1 and 2
        ListNode cur1 = list1;
        ListNode cur2 = list2;
        // Loop while either is not null
        while (cur1 != null || cur2 != null){
            if (cur1 == null){
                tail.next = cur2;
                cur2 = cur2.next;
                tail = tail.next;
                continue;
            } else if (cur2 == null){
                tail.next = cur1;
                cur1 = cur1.next;
                tail = tail.next;
                continue;
            }

            if (cur1.val == cur2.val){
                tail.next = cur1;
                cur1 = cur1.next;
                tail = tail.next;
                tail.next = cur2;
                cur2 = cur2.next;
                tail = tail.next;
            } else if (cur1.val >= cur2.val){
                tail.next = cur2;
                cur2 = cur2.next;
                tail = tail.next;
                tail.next = cur1;
                cur1 = cur1.next;
                tail = tail.next;
            } else {
                tail.next = cur1;
                cur1 = cur1.next;
                tail = tail.next;
                tail.next = cur2;
                cur2 = cur2.next;
                tail = tail.next;
            }
        }

        return head.next;
    }
}