# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head :
            return False

        signal1 = head
        signal2 = head
        
        # If both signals are not None 
        while signal2 and signal1 :

            if signal1 :
                signal1 = signal1.next

            if signal2 :
                if signal2.next :
                    signal2 = (signal2.next).next
             
            if signal1 == signal2 :
                return True

        return False        

