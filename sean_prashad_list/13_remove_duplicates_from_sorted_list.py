# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        
        while cur: #Outer Loop 
            while cur.next and cur.next.val == cur.val: #Inner Loop
                cur.next = cur.next.next
            cur = cur.next
        return head
        