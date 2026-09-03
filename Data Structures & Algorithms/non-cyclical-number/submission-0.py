class Solution:
    def isHappy(self, n: int) -> bool:
        book = {}
        while True:
            n = str(n)
            num = 0
            for i in n:
                num += int(i)**2    
            if num == 1:
                return True
            if num not in book:
                book[num] = 1
            else:
                return False
            
            n = num
            