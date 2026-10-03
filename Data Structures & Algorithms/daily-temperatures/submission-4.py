class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []
        results = []
        final = []
        for i in range(len(temperatures)):
            if len(arr) == 0:
                arr.append([temperatures[i], i])
            else:
                while len(arr) != 0 and arr[-1][0] < temperatures[i]:
                    cur = arr.pop()
                    diff = i - cur[1]
                    results.append([cur[1], diff])
                arr.append([temperatures[i], i])
        while len(arr) !=0:
            cur = arr.pop()
            results.append([cur[1], 0])
        results.sort()
        for i in results:
            final.append(i[1])

        return final
                