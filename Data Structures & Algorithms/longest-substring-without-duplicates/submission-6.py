class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        book = {}
        max_len = 1

        left = 0 
        for right in range(0, len(s)):
            if s[right] not in book:
                book[s[right]] = 1
            else:
                while book[s[right]] !=0:
                    book[s[left]] = 0
                    left+=1
                book[s[right]] = 1
            max_len = max(max_len, right - left+1)
    
        return max_len