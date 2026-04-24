# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Idea : 
        # Previous is None
        # curr is head
        # curr.next is head.next
        # We want that head does not point anymore to head.next
        # We want that head is now pointing to None ( previous )
        # we wanat to prev to be Head and curr should head.next
        # Due to the fact that 
        # def reverseList(self, head : Optional[ListNode]) -> Optional[ListNode] :
        #   prev = curr.next
        #   curr = prev 
        #   curr = curr.next # WRONG, curr.next is now prev, use a temp value
        
        if not head :
            return None 
        
        prev = None
        curr = head 

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev         






        