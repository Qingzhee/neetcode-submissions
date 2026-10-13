class Solution:
    def isValid(self, s: str) -> bool:
        book = {
            "]" :"[",
            ")" :"(",
            "}":"{"
        }
        stack = []
        starts = ["(", "[", "{"]
        for i in s:
            if i in starts:
                stack.append(i)
            else:
                if len(stack) == 0 or stack[-1] != book[i]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0