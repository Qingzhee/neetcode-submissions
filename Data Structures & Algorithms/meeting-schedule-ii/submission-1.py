"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        arr = []
        counter = 0

        for i in range(len(intervals)):
            if len(arr) == 0:
                heapq.heappush(arr, intervals[i].end)
            
            else:
                while arr and intervals[i].start>=arr[0]:
                    heapq.heappop(arr)
                heapq.heappush(arr, intervals[i].end)
            counter = max(counter, len(arr))
        return counter