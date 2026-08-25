class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        cur_max = 0
        for i in s:
            if i not in arr:
                arr.append(i)
                cur_max = max(cur_max, len(arr))
            else:
                ind = arr.index(i)
                if ind == len(arr)-1:
                    arr = [i]
                    continue
                arr = arr[ind+1:]
                arr.append(i)

        return cur_max