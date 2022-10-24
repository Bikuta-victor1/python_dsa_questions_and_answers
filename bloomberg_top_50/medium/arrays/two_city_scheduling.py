from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        refund = []
        minCost = 0 
        N = len(costs) // 2 

        for A, B in costs :
            refund.append(B- A)
            minCost += A
        refund.sort()

        for i in range(N):
            minCost += refund[i]
            
        return minCost