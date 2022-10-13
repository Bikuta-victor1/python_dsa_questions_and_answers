# Given an array of integers nums which is sorted in ascending order, and an integer target,

# write a function to search target in nums.

# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # My Solution 
        # for i in range(len(nums)):
        #     if nums[i] == target : 
        #         return i 
        # return -1
        
        l, r = 0, len(nums) - 1
        
        while l <= r : 
            m = (l + r ) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else: 
                return m
        return -1
    
    