# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(prev,head):
            if head:
                nexthead = head.next
                head.next = prev
        #         print(head.val)
                return reverse(head,nexthead)
            return prev
        return reverse(None,head)

     