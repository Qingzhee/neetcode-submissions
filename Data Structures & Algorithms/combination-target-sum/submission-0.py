class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        def backtrack(i, cur_sum, cur_comb):
            if cur_sum == target:
                arr.append(cur_comb.copy())
                return
            if cur_sum>target:
                return 
            if i > len(nums)-1:
                return

            backtrack(i+1, cur_sum, cur_comb)

            cur_sum = cur_sum + nums[i]
            cur_comb.append(nums[i])
            
            backtrack(i, cur_sum, cur_comb)
            cur_comb.pop()

        backtrack(0, 0, [])
        return arr