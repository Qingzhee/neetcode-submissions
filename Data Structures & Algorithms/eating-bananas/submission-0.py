class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        front = 0
        back = len(piles)-1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        front = 1
        back = max(piles)

        while front <= back:
            mid = (front + back) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                back = mid - 1
            else:
                front = mid + 1

        return front