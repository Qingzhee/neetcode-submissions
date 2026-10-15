class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        book = {}
        cur = 0

        left = 0
        for right in range(len(s)):
            book[s[right]] = book.get(s[right], 0)+ 1
            diff = right - left +1 - max(book.values())
            while right - left +1 - max(book.values()) >k:
                book[s[left]] -= 1
                left+=1
            
            cur = max(cur, right - left+ 1)

        return cur