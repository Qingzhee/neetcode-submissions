class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        
        def checker(r, c, k):
            if k == len(word):
                return True

            if r<0 or c<0 or r>=row or c>=col or board[r][c]!= word[k]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (checker(r-1,c,k+1) or checker(r+1,c,k+1) or checker(r,c+1,k+1) or checker(r,c-1,k+1))
            board[r][c] = temp

            return found

        for i in range(row):
            for j in range(col):
                if checker(i, j, 0):
                    return True

        return False



        
