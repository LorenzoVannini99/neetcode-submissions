# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Idea :
        # We have two linked lists
        # if not list_1 return list 2 and viceversa
        # Now we need to create the optimal routing such taht they are in ascending order
        # connect the nodeds accordingly
        # create a first ListNode
        # Head = ListNode()
        # Remember that by doing this, you are creating an object of classnode type
        # head is the pointer, since in python everthing is an object and the concept of reference and pointers 
        # is radically different from C and C++.
        # Head is the reference to that object, the instance of that class.
        # By doing curr = Head, you are creating 2 references to the SAME object .. ListNode() somewhere in memory
        
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val <= list2.val:
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







  








        