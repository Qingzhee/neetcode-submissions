class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_max = 0
        maxx = ""
        for i in range(0, len(s)):
            
            left, right= i-1, i+1
            while left>=0:
                if s[left] == s[i]:
                    if i - left+1 >cur_max:
                        cur_max = i - left+1
                        maxx = s[left:i+1]
                    left-=1
                else:
                    break
            
            while left>=0 and right <len(s):
                if s[left] == s[right]:
                    if right - left+1 >cur_max:
                        cur_max = right - left+1
                        maxx = s[left:right+1]

                    left -=1
                    right+=1
                else:
                    break
        
            # while right<len(s):
            #     if s[] == s[i]:
            #         if i - left+1 >cur_max:
            #             cur_max = i - left+1
            #             maxx = s[left:i+1]
            #         left-=1
            #     else:
            #         break

            if len(s[i])> cur_max:
                maxx = s[i]

        return maxx