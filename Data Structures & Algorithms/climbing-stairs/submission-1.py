class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(x):
            if x == 0:
                return 1
            if x < 0:
                return 0

            if x in memo:
                return memo[x]

            memo[x] = climb(x - 1) + climb(x - 2)
            return memo[x]

        return climb(n)