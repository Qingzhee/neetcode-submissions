class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums)-2):
            if i>0:
                if nums[i] == nums[i-1]:
                    continue
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left]+ nums[right] == target:
                    xx = [nums[i], nums[left], nums[right]]
                    if xx not in arr:
                        arr.append(xx)
                    left+=1
                    right-=1
                elif nums[left] + nums[right] < target:
                    left+=1
                else:
                    right-=1

        return arr