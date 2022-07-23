class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Time complexity: O(nlogn)
        # Space complexity: O(N)
        return sorted(s) == sorted(t)
        
        # Time complexity: O(n)
        # Space complexity: O(1)
        from collections import Counter
        return Counter(s) == Counter(t)

        # Time complexity: O(n)
        # Space complexity: O(n)
        s_hashMap = {}
        t_hashMap = {}
        
        for letter in s:
            if letter in s_hashMap:
                s_hashMap[letter] += 1
            else:
                s_hashMap[letter] = 1
                
        for letter in t:
            if letter in t_hashMap:
                t_hashMap[letter] += 1
            else:
                t_hashMap[letter] = 1
                
        return s_hashMap == t_hashMap
        
        # s_hashMap  = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        
        # t_hashMap  = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}