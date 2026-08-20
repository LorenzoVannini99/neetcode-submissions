# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Idea :
        # We have 2 heads and two curr: curr1 and curr2
        # create a third pointer called curr and create head
        # those two pointers will be the overall pointers'list
        # while both are not None 
        # if curr2.val >= curr1.val --> increment curr1
        # curr.val = curr1.val
        # else --> increment curr2 
        # curr.val = curr2.val
        # if one of the two curr, become None
        # the remaining list is added

        if not list1 :
            return list2
        if not list2 :
            return list1

        head = ListNode()
        curr = head 

        while list1 and list2:

            if list1.val <= list2.val :
                curr.next = list1
                list1 = list1.next

            else :
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        if list1 :
            curr.next = list1

        if list2:
            curr.next = list2

        return head.next      
        










        