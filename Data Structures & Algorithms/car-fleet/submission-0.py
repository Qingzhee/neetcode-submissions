class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        stack = []
        comb = []
        for i in range(len(position)):
            comb.append([position[i], speed[i]])
        comb.sort(reverse = True)
    
        for i in range(len(comb)):
            dist = target - comb[i][0]
            time = dist/comb[i][1]
            if len(stack) == 0:
                stack.append(time)
            else:
                if time > stack[-1]:
                    count+=1
                    stack = []
                    stack.append(time)

        return count + 1