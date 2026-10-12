class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        book = {}
        starts = []
        maxx = 1
        for i in range(len(nums)):
            if nums[i] not in book:
                book[nums[i]] = 1
        for i in range(len(nums)):
            prev = nums[i]-1
            if prev not in book:
                starts.append(nums[i])
        for i in starts:
            cur = 1
            cur_num = i
            while cur_num+1 in book:
                cur+=1
                cur_num+=1
            maxx = max(maxx, cur)
        return maxx


