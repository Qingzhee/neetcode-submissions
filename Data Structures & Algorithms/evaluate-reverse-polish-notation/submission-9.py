class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*','/']
        arr = []
        for i in tokens:
            if i in ops:
                x2 = arr.pop()
                x1 = arr.pop()
                if i == "+":
                    arr.append(x1+x2)
                elif i == "-":
                    arr.append(x1-x2)
                elif i == "*":
                    arr.append(x1*x2)
                else:
                    arr.append(int(x1/x2))
            else:
                arr.append(int(i))
            
        return arr.pop()
