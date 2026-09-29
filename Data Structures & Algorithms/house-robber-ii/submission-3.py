class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        arr = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)-1):
            max_money = max(arr[i-2]+nums[i], arr[i-1])
            arr.append(max_money)

        arr2 = [0, nums[1], max(nums[1], nums[2])]
        for i in range(3, len(nums)):
            max_money = max(arr2[i-2]+nums[i], arr2[i-1])
            arr2.append(max_money)
        

        return max(arr[-1], arr2[-1])