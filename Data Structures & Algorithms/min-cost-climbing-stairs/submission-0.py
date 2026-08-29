class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0,0]
        for i in range(2, len(cost)+1):
            min_cost = min(cost[i-1]+ arr[-1], cost[i-2]+ arr[-2])
            arr.append(min_cost)

        return arr[-1]

        