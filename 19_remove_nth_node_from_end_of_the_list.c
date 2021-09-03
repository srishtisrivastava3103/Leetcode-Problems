# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* temp=head;
    struct ListNode* ptr=head;
    struct ListNode* pptr=head;
    int c=0;
    while(temp!=NULL)
    {   c+=1;
        temp=temp->next;
    }
    if (c==n)
    {
        return head->next;
    }
    while(c-n>0)
    {
        pptr=ptr;
        ptr=ptr->next;
        c-=1;
    }
    pptr->next=ptr->next;
    return head;

}

