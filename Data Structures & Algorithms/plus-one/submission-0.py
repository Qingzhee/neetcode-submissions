class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        num = 0
        for i in digits:
            num += i * (10**n)
            n -= 1
        num+=1
        num_str = str(num)
        arr = []
        for i in num_str:
            arr.append(i)
        return arr
