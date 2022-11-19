

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 

# return the minimum number of conference rooms required.

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[0])

        heap = []
        for x, y in intervals: 
            if not heap  or heap[0] > x: 
                # when there is an existing meeting that has its end time overlapping with the next meeting start time, we add to the queue
                heapq.heappush(heap, y)
                # when the existing meeting ends before the next meeting starts, we replace the existing time 
            else: 
                heapq.heappushpop(heap, y)
        return len(heap)
