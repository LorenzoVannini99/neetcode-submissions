# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
    
        # Idea :
        # Start both slow (s) and fast (f) at the same position (the head).

        # Move fast ahead n steps first.
        # This makes fast and slow separated by exactly n nodes.

        # Then move both pointers together, one step at a time.
        # When fast reaches the end (None), slow will be just before the node we need to remove.
        
        # PROBLEM :
        # if n == list size we have a problem
        # If we use a dummy node 
        # we keep the same algorithm but moving f n + 1 times not n
        
        if not head :
            return 

        # First check if LL contains cycle
        def HasCycle( head ):
        
            slow = head
            fast = head
        
            while slow and fast :

                if fast.next :
                    fast = fast.next
                    return False

                if fast.next :
                    fast = fast.next
                    return False    

                slow = slow.next

                if slow == fast :
                    return True
        
        if HasCycle ( head = head ) :
            return False
        
        else :
            
            dummy = ListNode()
            dummy.next = head
            slow = dummy
            fast = dummy

            for _ in range( n + 1 ) :
                fast = fast.next

            while fast :
                fast = fast.next
                slow = slow.next

            slow.next = slow.next.next

            return dummy.next        






                

        


                   


        
        