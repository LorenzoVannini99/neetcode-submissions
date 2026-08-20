# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_digits = []
        l2_digits = []

        curr1 = l1
        curr2 = l2

        while curr1 :
            l1_digits.append(curr1.val) # [1,2,3]
            curr1 = curr1.next

        while curr2 :
            l2_digits.append(curr2.val) # [4,5,6] 
            curr2 = curr2.next  

        numb1 = 0
        numb2 = 0

        for i in range(len( l1_digits )):
            numb1 = numb1 + l1_digits[i] * 10 ** (i)
        
        for i in range(len( l2_digits )):
            numb2 = numb2 + l2_digits[i] * 10 ** (i)
        
        numb = numb1 + numb2
        
        if numb == 0 :
            return ListNode(0)

        l_digit = [int(ch) for ch in str(numb) ]
        l_digit.reverse()

        l = ListNode()
        curr = l

        for i in range(len(l_digit)) :
            curr.next = ListNode ( l_digit[i] )
            curr = curr.next
            
        return l.next

