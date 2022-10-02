# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        # since fast = 2(slow),we can stop when fast becomes null, meaning it's the end of the array
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        return slow 
        