class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(board):
            for i in board:
                book = {}
                for j in i:
                    if j == ".":
                        continue
                    if j not in book:
                        book[j] = 1
                    else:
                        return False
            return True

        def checkCol(board):
            for i in range(9):
                book = {}
                for j in range(9):
                    if board[j][i] == ".":
                        continue
                    if board[j][i] not in book:
                        book[board[j][i]] = 1
                    else:
                        return False
            return True


        def checkSubBox(board):
            boxes = [{} for _ in range(9)]
            for row in range(9):
                for col in range(9):
                    val = board[row][col]
                    if val == '.':
                        continue
                    box_id = (row // 3) * 3 + (col // 3)
                    if val not in boxes[box_id]:
                        boxes[box_id][val] = 1
                    else:
                        return False
            return True

        return checkRow(board) and checkCol(board) and checkSubBox(board)
