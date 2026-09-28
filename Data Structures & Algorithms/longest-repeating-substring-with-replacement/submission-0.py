class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        book = {}
        for right in range(len(s)):
            book[s[right]] = book.get(s[right], 0)+1
            # check difference
            book = dict(sorted(book.items(), key=lambda x: x[1], reverse=True))

            total_diff = 0
            cur = 0
            for kk,v in book.items():
                if cur == 0:
                    cur+=1
                else:
                    total_diff+=v

            if total_diff <= k:
                cur_len = right - left +1
                if cur_len>max_len:
                    max_len = cur_len
                
            else:
                book[s[left]] -=1
                left +=1
                
        return max_len