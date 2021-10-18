# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        A=head
        B = k
        temp = A
        count = 0
        if A==None or A.next==None or B==0:
            return A
    
        while temp!=None:
            temp = temp.next
            count+=1
        if B%count==0:
            return A
        bp = abs(count - B%count)
        
        temp = A
        c = 0
        prev =  temp
        while c<bp:
            prev = temp
            temp = temp.next
            c+=1
        prev.next = None
        new_head = temp
        while temp.next!=None:
            temp = temp.next
        temp.next = A
        
        return new_head
        