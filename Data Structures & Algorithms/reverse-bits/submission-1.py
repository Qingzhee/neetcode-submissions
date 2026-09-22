class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:]
        extra = 32-len(str(x))
        for i in range(extra):
            x = "0" + x
        
        return(int(str(x)[::-1],2))

