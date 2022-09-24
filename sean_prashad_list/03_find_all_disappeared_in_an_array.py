# Given an array nums of n integers where nums[i] is in the range [1, n],
#  return an array of all the integers in the range [1, n] that do not appear in nums.
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappearednum = []
        
        for n in nums: 
            i = abs(n) -1
            nums[i]= -1 * abs(nums[i]) 
        
        for i, n in enumerate(nums): 
            if n > 0: 
                disappearednum.append(i+1)
            
        return disappearednum       
        