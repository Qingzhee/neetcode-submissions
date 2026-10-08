class Solution:
    def canJump(self, nums: List[int]) -> bool:
        book = {}
        def jump(i):
            if i >= len(nums)-1:
                return True
            if i in book:
                return book[i]
            
            for j in range(1, nums[i]+1):
                if jump(i+j):
                    book[i] = True
                    return True
            book[i] = False
            return False
        return jump(0)
