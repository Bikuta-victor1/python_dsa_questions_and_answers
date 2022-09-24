# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums: 
            res = n ^ res
        return res
        
#         hashset = set()
        
#         for n in nums: 
#             if n not in hashset: 
#                 hashset.add(n)
#             else:
#                 hashset.discard(n)
#         return min(hashset)