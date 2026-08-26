class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        back = len(nums)-1
        while front<=back:
            mid = int((front+back)/2)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                front = mid+1
            else:
                back = mid-1
        return -1
