class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n) 
        n = 0
        for i in range(2, len(bits)):
            if bits[i] == "1":
                n+=1
        return n