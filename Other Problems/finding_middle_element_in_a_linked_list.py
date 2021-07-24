# https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

# function should return index to the any valid peak element
def findMid(head):
    # Code here
    # return the value stored in the middle node
    ptr = head
    pptr = head
    while pptr!=None and pptr.next!=None:
        ptr = ptr.next
        pptr = pptr.next.next
    return ptr.data

