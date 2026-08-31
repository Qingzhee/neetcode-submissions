class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(start, end):
            memo = {}

            def robbed(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                skip = robbed(i + 1)
                take = nums[i] + robbed(i + 2)

                memo[i] = max(skip, take)
                return memo[i]

            return robbed(start)

        take_first_option = rob_range(0, len(nums) - 2)
        take_last_option = rob_range(1, len(nums) - 1)

        return max(take_first_option, take_last_option)