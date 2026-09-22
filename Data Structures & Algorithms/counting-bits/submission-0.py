class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(0, n+1):
            arr.append(bin(i).count("1"))
        return arr