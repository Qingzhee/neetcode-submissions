class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if i == "[" or i == "{" or i == "(":
                arr.append(i)
            elif i == "]" or i == "}" or i == ")":
                if len(arr) == 0:
                    return False
                elif i == "]" and arr[-1] == "[":
                    arr.pop()
                elif i == "}" and arr[-1] == "{":
                    arr.pop()
                elif i == ")" and arr[-1] == "(":
                    arr.pop()
                else: return False

        return len(arr) == 0