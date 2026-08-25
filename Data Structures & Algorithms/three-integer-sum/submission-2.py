class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums) - 2):
            front = i + 1
            back = len(nums) - 1
            target = 0 - nums[i]

            while front < back:
                total = nums[front] + nums[back]

                if total == target:
                    arr = [nums[i]]
                    arr.append(nums[front])
                    arr.append(nums[back])

                    if arr not in out:
                        out.append(arr)

                    front += 1
                    back -= 1

                elif target > total:
                    front += 1

                else:
                    back -= 1

        return out
                