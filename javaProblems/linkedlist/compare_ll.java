/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public int solve(ListNode A, ListNode B) {
        ListNode h1 = A;
        ListNode h2 = B;
        while (h1 != null || h2 != null){
            if (h1.val != h2.val){
                return 0;
            }
            h1 = h1.next;
            h2 = h2.next;
        }
        if (h1 != null || h2 != null){
            return 0;
        }
        return 1;
    }
}
