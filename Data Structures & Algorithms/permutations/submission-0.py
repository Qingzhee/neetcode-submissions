class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def perm(cur):
            if len(cur) == len(nums):
                arr.append(cur.copy())
                return
            
            for i in nums:
                if i not in cur:
                    cur.append(i)
                    perm(cur)
                    cur.pop()

        perm([])
        return arr
        