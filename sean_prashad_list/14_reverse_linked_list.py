# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        #Recursive Method
#         def reverse(curr, prev):
#             if not curr: 
#                 return prev
#             else:
#                 next = curr.next
#                 curr.next = prev
                
#             return reverse(next, curr)
#         return reverse(head, None)
    
        prev = None 
        slow = head
        #Iterative method
        while slow: 
            temp = slow.next
            slow.next = prev 
            prev = slow
            slow = temp
        return prev