class Solution:
    # @param A : head node of linked list
    def solve(self, A):
        head = A
        while head != None:
            print(head.val, end=" ")
            head = head.next
        print()
