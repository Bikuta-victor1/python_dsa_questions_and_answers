
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 

# There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. 

# If such a character does not exist, return the first character in letters.


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
          # if the number is out of bound
          #            -1 gives the last number in the array 
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = (high+low)//2
            
            if  target >= letters[mid]: # in binary search this would be only greater than
                low = mid+1
            
            if target < letters[mid]:
                high = mid-1
                
        return letters[low]
        

            