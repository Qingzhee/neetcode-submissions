import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # large can use normally
        # small has to be -ve
        if len(self.small) == 0 and len(self.large) == 0:
            heapq.heappush(self.large, num)
        elif len(self.small) == 0. and len(self.large) == 1:
            compare = heapq.heappop(self.large) 
            if num>compare:
                heapq.heappush(self.large, num)
                heapq.heappush(self.small, -compare)
            else:
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, compare)
            
        elif len(self.small) == len(self.large):
            compare_small = -heapq.heappop(self.small)
            compare_big = heapq.heappop(self.large)
            if num < compare_small :
                    heapq.heappush(self.small, -num)
                    heapq.heappush(self.small, -compare_small)
                    heapq.heappush(self.large, compare_big)
            else:
                heapq.heappush(self.small, -compare_small)
                heapq.heappush(self.large, compare_big)
                heapq.heappush(self.large, num)

        elif len(self.large) < len(self.small):
            compare = -heapq.heappop(self.small)
            if num < compare:
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, compare)
            else:
                heapq.heappush(self.small, -compare)
                heapq.heappush(self.large, num)

        elif len(self.large) > len(self.small):
            compare = heapq.heappop(self.large)
            if num < compare:
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, compare)
            else:
                heapq.heappush(self.small, -compare)
                heapq.heappush(self.large, num)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] + (-self.small[0])) /2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]











        