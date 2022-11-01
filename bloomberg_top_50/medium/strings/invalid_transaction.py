# A transaction is possibly invalid if:

# the amount exceeds $1000, or;

# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

# You are given an array of strings transaction where transactions[i] 

# consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order

from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transactionMap = defaultdict(set)
        invalid = []
        
        #Creating a map to keep track of the 3 values at once 
        for s in transactions:
            name, time, amount, city = s.split(",")
            time = int(time)
            transactionMap[(time, name)].add(city)
        
        for s in transactions:
            name, time, amount, city = s.split(",")
            amount = int(amount)
            time = int(time)
            
            #Check for invalid prices   
            if amount > 1000:
                invalid.append(s)
                continue #starts on the next loop immediately 
            
            # check for suspicious transaction in same time bracket(t-60 to t+60) by same user
            for t in range(time-60 , time+60 ):                
                if (t, name) not in transactionMap:
                    continue
                else:
                    dcity = transactionMap[(t, name)]
                 
                # if the key(time, name) has more than one city in the same time bracket or if the 0th or only of value of the city array is not the current city
                if len(dcity) > 1 or next(iter(dcity)) != city: 
                    invalid.append(s)
                    break
            
        return invalid
            
            
        
        