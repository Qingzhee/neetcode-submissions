class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        book = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            book[s[right]] = book.get(s[right], 0)+1

            diff = right-left + 1 - max(book.values())
            
            if diff>k:
                book[s[left]] -=1
                left +=1
            else:
                max_len = max(max_len, right -left +1)
        return max_len