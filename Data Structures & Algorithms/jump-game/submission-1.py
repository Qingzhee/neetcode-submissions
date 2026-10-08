class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, j in enumerate(nums):
            if i>reach:
                return False
            reach = max(i+j, reach)
        return True