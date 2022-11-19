# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.

# bool insert(int val) Inserts an item val into the set if not present. 

# Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. 

# Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements it's guaranteed that at least one element exists when this method is called). 

# Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.


import random


class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res: 
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res: 
            idx = self.numMap[val] #Get index of val from map
            lastVal = self.numList[-1] # get the last val of the list 
            self.numMap[lastVal] = idx #assign the val index to that of the last of the last val 
            self.numList[idx] = lastVal # change the postion of the val in the array to the lastVal  
            self.numList.pop() #pop the last val now from the array 
            del self.numMap[val]     # remove from the map too 
        return res
    
    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()