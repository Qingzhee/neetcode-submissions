class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        out = []

        for i in range(0, len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                total = nums[left]+nums[right]
                if total == target:
                    if [nums[i], nums[left], nums[right]] not in out:
                        out.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    continue
                if total < target:
                    left+=1
                else:
                    right-=1
                
        return out

        