# https://www.interviewbit.com/problems/palindrome-list/

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        u = A
        l = A
        c = 0
        if A.next == None:
            return 1

        while(u.next!=None):
            u = u.next
            c+=1
        if c%2==0:
            half = c//2
        else:
            half = (c//2)+1
        sec = A
        c = 0
        while c<half:
            prev = sec
            sec = sec.next
            c+=1
        curr = sec
        currnext = sec.next
        t = prev
    
        while curr.next!=None:
            currnext = curr.next
            curr.next = prev
            prev = curr
            curr = currnext
        t.next = curr
        curr.next = prev
        sec.next = None
        k = curr
    
        temp = A
    
        # while temp!=None:
        #     print(temp.val)
        #     temp = temp.next
        
        while curr!= None and l!=k:
            if curr.val != l.val:
                return 0
            curr = curr.next
            l = l.next
        return 1
