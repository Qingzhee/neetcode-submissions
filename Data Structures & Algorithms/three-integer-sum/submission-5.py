class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    trip = nums[i], nums[left], nums[right]
                    if trip not in out:
                        out.append(trip)
                    left += 1
                    right -= 1
                elif s > target:
                    right -= 1
                else:
                    left += 1

        return out 