# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

# You may assume all four edges of the grid are all surrounded by water.

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: 
            return
        
        rows, columns = len(grid) , len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r , c):      
            q = collections.deque()    
            
            visit.add((r,c))
            q.append((r, c))
             
            while q: 
                row , col = q.popleft()
                directions = [[-1,0], [1,0], [0,1],[0,-1]]
                
                for dr, dc in directions: 
                    ro, co = row + dr, col + dc
                    if ro in range(rows) and co in range(columns) and grid[ro][co] == "1" and (ro,co) not in visit: 
                        q.append((ro,co))
                        visit.add((ro,co))
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r, c) not in visit: 
                    bfs(r, c)
                    islands += 1
        return islands