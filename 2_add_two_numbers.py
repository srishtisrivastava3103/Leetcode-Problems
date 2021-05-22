# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        A = l1
        B = l2
        temp = A
        a = ''
        while temp!=None:
            a+=str(temp.val)
            temp = temp.next
        temp = B
        b = ''
        while temp!=None:
            b+=str(temp.val)
            temp = temp.next
        s =  str(int(a[::-1])+int(b[::-1]))[::-1]
        temp = ListNode(int(s[0]))
        head = temp
        for i in range(1,len(s)):
            temp.next = ListNode(int(s[i]))
            temp = temp.next
        return head
