class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        book = {}
        for i in range(0, len(s)):
            counter += 1
            left = i - 1
            right = i + 1

            while left >= 0 and s[left] == s[i]:
                sub = (left, i)      
                if sub not in book:
                    book[sub] = 1
                    counter += 1
                left -= 1

            # while right < len(s) and s[right] == s[i]:
            #     sub = (i, right)         
            #     if sub not in book:
            #         book[sub] = 1
            #         counter += 1
            #     right += 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                sub = (left, right)     
                if sub not in book:
                    book[sub] = 1
                    counter += 1
                right += 1
                left -= 1

        return counter