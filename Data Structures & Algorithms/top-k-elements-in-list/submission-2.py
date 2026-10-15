import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = {}
        # {1: 1, 2: 2, 3: 3}
        for i in nums:
            book[i] = book.get(i, 0)+1
        arr = []
        for key,val in book.items():
            heapq.heappush(arr, [-val,key])
        ans = []
        for i in range(k):
            x = heapq.heappop(arr)
            ans.append(x[1])
        return ans
