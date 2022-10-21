# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
         
        
#         dict = {}
        
#         for i in s:                       
#             if i not in dict: 
#                 dict[i] = 1       
#             else:
#                 dict[i] += 1
                
#         for i in range(len(s)):
#             if dict[s[i]] == 1:
#                 return i
            
#         return -1
        
        cnt = Counter(s)
    
    
        for i, r in enumerate(s):
            if cnt[r] == 1:
                return i
            
        return -1
        
    
    
                
                
            