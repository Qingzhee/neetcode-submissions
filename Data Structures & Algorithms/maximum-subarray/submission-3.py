class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = max(nums)
        cur = 0
        left = 0
        for right in range(len(nums)):
            cur+=nums[right]
            cur_max = max(cur_max, cur)
            
            while cur <0 and left<=right:
                cur-=nums[left]
                left+=1
        return cur_max
