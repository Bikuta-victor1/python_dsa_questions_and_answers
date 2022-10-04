# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            
        prev = None   
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        left,right = head, prev
        while right :
            if left.val != right.val:
                return False
            left  = left.next
            right = right.next
        return True
            
        
        
        
#         nums = []
#         # slow, fast = head, head
        
#         while head:
#             nums.append(head.val)
#             head = head.next
        
#         l, r = 0, len(nums) -1 
        
#         while l<=r:
#             if nums[l] != nums[r]:
#                 return False
#             else:
#                 l += 1
#                 r -= 1
#         return True
