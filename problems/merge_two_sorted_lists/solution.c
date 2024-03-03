/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;
    struct ListNode* mergeList = NULL;
   if(list1->val <= list2->val){
       mergeList=list1;
       mergeList->next=mergeTwoLists(list1->next,list2);
   }else{
       mergeList=list2;
       mergeList->next=mergeTwoLists(list1,list2->next);
   }
   return mergeList;
}