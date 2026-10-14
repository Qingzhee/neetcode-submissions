class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def checker(r, c, i):
            
            if r<0 or r >len(board)-1:
                return False
            if c<0 or c> len(board[0])-1:
                return False
            if board[r][c] != word[i]:
                return False
            if board[r][c] == word[i]:
                if i == len(word)-1:
                    return True
            holder = board[r][c]
            board[r][c] = "#"
            found = (
                    checker(r-1, c, i+1) or
                    checker(r+1, c, i+1) or
                    checker(r, c-1, i+1) or
                    checker(r, c+1, i+1)
                ) 
            board[r][c] = holder
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if checker(i, j, 0):
                    return True

        return False