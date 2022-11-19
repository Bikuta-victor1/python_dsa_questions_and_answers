# Design a Leaderboard class, which has 3 functions:

# addScore(playerId, score): Update the leaderboard by adding score to the given player's score.

# If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.

# top(K): Return the score sum of the top K players.
# reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). 

# It is guaranteed that the player was added to the leaderboard before calling this function.
# Initially, the leaderboard is empty.


import heapq
from typing import Collection


class Leaderboard:

    def __init__(self):
        self.dic = Collection.defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] +=score
        

    def top(self, K: int) -> int:

        heap =[]
        for v in self.dic.values():
            heapq.heappush(heap, v )
        while len(heap) > K: 
            heapq.heappop(heap)
        res = 0 
        while(heap): 
            res += heapq.heappop(heap)
        
        return res 
        

    def reset(self, playerId: int) -> None:
        del self.dic[playerId]