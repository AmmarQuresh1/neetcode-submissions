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
        ListNode list3 = null;
        // Assign current pointers for list1 and 2
        ListNode cur1 = list1;
        ListNode cur2 = list2;
        // Loop while either is not null
        while (cur1 != null || cur2 != null){
            if (cur1 == null){
                list3 = cur2.val;
                cur2 = cur2.next;
                list3 = list3.next;
                continue;
            } else if (cur2 == null){
                list3 = cur1.val;
                cur1 = cur1.next;
                list3 = list3.next;
                continue;
            }

            if (cur1.val == cur2.val){
                list3 = cur1.val;
                list3 = list3.next;
                list3 = cur2.val;
            } else if (cur1.val >= cur2.val){
                list3 = cur2.val;
                list3 = list3.next;
                list3 = cur1.val;
            } else {
                list3 = cur1.val;
                list3 = list3.next;
                list3 = cur2.val;
            }

            list3 = list3.next;
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
    }
}