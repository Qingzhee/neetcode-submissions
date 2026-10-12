class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = False
        zero2 = False
        zero_idx = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero==True:
                    zero2 =True
                zero = True
                zero_idx = i
            else:
                total*=nums[i]
        
        if zero2:
            return [0]*len(nums)

        for i in range(len(nums)):
            if zero == True:
                if i == zero_idx:
                    nums[i] = int(total)
                else:
                    nums[i] = 0
            else:
                nums[i] = int(total/nums[i])
        return nums