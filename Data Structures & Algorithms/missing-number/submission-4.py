class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            # 0,1,2

            total+=nums[i]
            total-=(i+1)
        return -total