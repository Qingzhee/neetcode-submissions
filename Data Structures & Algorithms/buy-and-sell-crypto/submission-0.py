class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 0
        max_diff = 0
        for i in range(1, len(prices)):
            if prices[i]-prices[cur]<=0:
                cur = i
            if prices[i] - prices[cur] > max_diff:
                max_diff = prices[i] - prices[cur]
        return max_diff
