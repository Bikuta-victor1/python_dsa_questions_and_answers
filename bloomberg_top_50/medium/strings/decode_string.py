# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 

# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

class Solution:
    def decodeString(self, s: str) -> str:
        
        if not s: 
            return 
        
        stack= []
        currStr = ""
        currNum = 0
        
        for c in s: 
            if c == "[":
                stack.append(currStr)
                stack.append(currNum)
                currNum = 0
                currStr = ""               
            elif c == "]":
                prevNum = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + prevNum * currStr
            elif c.isdigit():
                currNum = currNum*10 + int(c)
            else :
                currStr += c
                
        return currStr
        