class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_cur, max_cur = 1,1
        for i in nums:
            if i ==0:
                min_cur, max_cur = 1,1
            temp = max_cur
            max_cur = max(max_cur*i, min_cur*i, i)
            min_cur = min(temp*i, min_cur*i, i)

            res = max(res, max_cur, min_cur)

        return res