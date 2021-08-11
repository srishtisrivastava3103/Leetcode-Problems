# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#This is the faster method where we reverse the first half of the linked list instead of second half.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
        length,node = 0,head
        while node:
            node=node.next
            length+=1
        mid = length//2

        # reverse 1st half
        prev,node=None,head
        for _ in range(mid):
            node.next,node,prev = prev,node.next,node

        left=prev
        right=node if length%2==0 else node.next

        while left:
            if left.val != right.val:
                return False
            left,right = left.next, right.next

        return True
