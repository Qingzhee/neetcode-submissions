class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []

        def subset(i, cur):
            if i == len(nums):
                arr.append(cur.copy())
                return

            cur.append(nums[i])
            subset(i + 1, cur)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            subset(i + 1, cur)

        subset(0, [])
        return arr