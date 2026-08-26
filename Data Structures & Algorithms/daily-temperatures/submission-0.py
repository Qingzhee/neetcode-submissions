class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        book = []
        ans_pre = []
        for i in range(len(temperatures)):

            if len(book)>0 and temperatures[i]>book[-1][0]:
                while len(book)>0 and temperatures[i]>book[-1][0]:
                    popped = book.pop()
                    popped.append(i-popped[1])
                    ans_pre.append(popped)
                book.append([temperatures[i], i])
                continue
            book.append([temperatures[i], i])
        while len(book)>0:
            popped = book.pop()
            popped.append(0)
            ans_pre.append(popped)
        ans_pre.sort(key=lambda x: x[1])
        ans=[]
        for i in ans_pre:
            ans.append(i[2])
        return ans
        