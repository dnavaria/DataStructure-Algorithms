# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return an integer
    def solve(self, A, B):
        h1 = A
        h2 = B
        while h1 is not None or h2 is not None:
            if h1.val != h2.val:
                return 0
            h1 = h1.next
            h2 = h2.next
        if h1 is not None or h2 is not None:
            return 0
        return 1
