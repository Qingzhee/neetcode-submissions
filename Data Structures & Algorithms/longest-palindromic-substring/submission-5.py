class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s
        cur_len = 0
        cur_string = ""

        for i in range(0, len(s)):
            left = i - 1
            right = i + 1
            cur = 1

            while left >=0 and s[left] == s[i]:
                cur+=1
                left-=1
            while right<len(s) and s[right] == s[i]:
                cur+=1
                right+=1

            if cur>cur_len:
                cur_len = cur
                cur_string = s[left+1 : right]
            
            while left>=0 and right<len(s):
                if s[left] == s[right]:
                    cur+=2
                    if cur>cur_len:
                        cur_len = cur
                        cur_string = s[left:right+1]
                    left-=1
                    right+=1
                    
                else:
                    break
        return cur_string               
                    