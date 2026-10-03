class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        opens = ["(", "{", "["]
        closes = [")", "}", "]"]
        for i in s:

            if i in opens:
                arr.append(i)
            else:
                if len(arr)<=0:
                    return False
                if arr[-1] != opens[closes.index(i)]:
                    return False
                arr.pop()
        return len(arr) == 0 