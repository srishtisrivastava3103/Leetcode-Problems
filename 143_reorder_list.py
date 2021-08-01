#https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = [head]
        ptr = head.next
        while ptr!=None:
            l.append(ptr)
            ptr = ptr.next
            
        while head and head.next and head.next.next:
            last = l.pop()
            last.next = head.next
            head.next = last
            prelast = l[-1]
            prelast.next = None
            head = head.next.next
            
                
#  Method - 2, gives TLE at last test case       
        
        
        
#         last = head.next
#         prelast = head
#         while head and head.next and head.next.next!=None:
#             while last.next!=None:
#                 prelast = last
#                 last = last.next
#             last.next = head.next
#             prelast.next = None

#             head.next = last
#             head = head.next.next
#     #         print(head.val,head.next.val)
#     #         print(last.val,last.next.val)
#             if head==None:
#                 break

#Method -3 Reverse and Merge
            
