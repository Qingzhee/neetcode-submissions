class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        cur_max = nums[0]
        cur_window = nums[0]

        for right in range(1, len(nums)):
            cur_window = max(nums[right], cur_window + nums[right])
            cur_max = max(cur_max, cur_window)
        return cur_max
