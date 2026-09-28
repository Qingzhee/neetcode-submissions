class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        book = {}
        longest = 0 

        for right in range(len(s)):
            char = s[right]
            book[char] = book.get(char, 0) + 1
            
            while book[char] == 2:
                book[s[left]] -=1
                left +=1
            longest = max(longest, right - left +1)

        return longest