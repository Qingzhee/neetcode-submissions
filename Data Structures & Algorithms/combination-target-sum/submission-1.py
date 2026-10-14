class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def comb (i, arr, count):
            if i>len(nums)-1 or count > target:
                return
            if count == target:
                output.append(arr.copy())
                return
            arr.append(nums[i])
            comb(i, arr, count+nums[i])
            arr.pop()
            comb(i+1, arr, count)
        
        comb(0, [], 0)
        return output