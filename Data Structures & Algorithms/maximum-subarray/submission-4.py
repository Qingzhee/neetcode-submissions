class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = max(nums)
        cur = 0
        left = 0
        for right in range(len(nums)):
            cur+=nums[right]
            cur_max = max(cur_max, cur)
            
            if cur<0:
                cur = 0
        return cur_max
