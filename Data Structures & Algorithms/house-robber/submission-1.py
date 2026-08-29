class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def robbed(i):
            if i >=len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = max(robbed(i+1), nums[i] + robbed(i+2))
            
            return memo[i]
        return robbed(0)