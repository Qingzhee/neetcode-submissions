import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap)>1:
            largest = -heapq.heappop(heap)
            next_largest = -heapq.heappop(heap)
            new = largest - next_largest
            if new>0:
                heapq.heappush(heap, -new)

        if len(heap) == 1:
            return -heap[0]
        else:
            return 0