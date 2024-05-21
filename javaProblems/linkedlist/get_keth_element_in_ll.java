/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public int solve(ListNode A, int B) {
        if(A==null){
            return -1;
        }
        int size=0;
        while(size<B){
            A=A.next;
            size++;
        }
        return A.val;
    }
}