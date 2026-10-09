class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1
        intervals.insert(i, newInterval)

        cur = 0
        while cur<len(intervals)-1:
            if intervals[cur][1]>= intervals[cur+1][0]:
                back = max(intervals[cur+1][1], intervals[cur][1])
                intervals[cur] = [intervals[cur][0], back]
                del intervals[cur+1]
            else:
                cur+=1

        return intervals





