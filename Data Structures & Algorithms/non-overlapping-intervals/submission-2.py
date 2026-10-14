class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        print(intervals)
        i = 0
        counter = 0
        while i < len(intervals)-1:
            if intervals[i][1]>intervals[i+1][0]:
                if intervals[i][1]> intervals[i+1][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
                counter+=1
                continue
            i+=1
        return counter
