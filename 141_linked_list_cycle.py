# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        sptr = head
        fptr = head.next
        while fptr and sptr and fptr.next and fptr!=sptr:
            fptr = fptr.next.next
            sptr = sptr.next
        if fptr==sptr:
            return True
        return False
        