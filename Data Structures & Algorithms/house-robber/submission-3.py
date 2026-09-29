class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        arr = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            max_money = max(nums[i]+ arr[i-2], arr[i-1])
            arr.append(max_money)

        return arr[-1]