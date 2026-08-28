import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            dist = ((i[0])**2 + (i[1])**2)**(1/2)
            heapq.heappush(heap, (dist, i))

        ans = []
        for i in range(k):
            dist, i = heapq.heappop(heap)
            ans.append(i)

        return ans