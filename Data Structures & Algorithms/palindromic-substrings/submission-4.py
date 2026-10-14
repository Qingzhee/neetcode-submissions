class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(0, len(s)):
            counter +=1

            left, right = i-1, i+1

            while left >= 0:
                if s[left] == s[i]:
                    counter +=1
                    left-=1
                else:
                    break
            
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    counter+=1
                    left-=1
                    right+=1
                else:
                    break
        return counter