/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
import BaseDataStructures.ListNode;

public class SearchInLinkedList {
    public int solve(ListNode A, int B) {
        while(A != null){
            if (A.val == B){
                return 1;
            }
            A = A.next;
        }
        return 0;
    }
}
