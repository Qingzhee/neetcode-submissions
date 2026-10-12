class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        needed = {}
        for i in t:
            needed[i] = needed.get(i,0)+1

        have = {}
        uniques = 0
        n = len(needed)
        left = 0
        min_arr = ""
        for right in range(len(s)):
            have[s[right]] = have.get(s[right], 0)+1
            if s[right] in needed and have[s[right]] == needed[s[right]]:
                uniques +=1

            if uniques == n:
                while True:
                    cur = s[left]
                    if cur in needed and have[cur] == needed[cur]:
                        break
                    have[cur] -= 1
                    left+=1

                if min_arr == "" or right - left +1 < len(min_arr):
                    min_arr = s[left:right+1]

        return min_arr





                
            