class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])

        right = True
        down = left = up = False

        arr = []
        row, col = 0, 0
        lef, rig = 0, n - 1
        top, bot = 0, m - 1

        while len(arr) < m * n:
            arr.append(matrix[row][col])

            if right:
                if col == rig:
                    right = False
                    down = True
                    top += 1
                    row += 1
                else:
                    col += 1

            elif down:
                if row == bot:
                    down = False
                    left = True
                    rig -= 1
                    col -= 1
                else:
                    row += 1

            elif left:
                if col == lef:
                    left = False
                    up = True
                    bot -= 1
                    row -= 1
                else:
                    col -= 1

            elif up:
                if row == top:
                    up = False
                    right = True
                    lef += 1
                    col += 1
                else:
                    row -= 1

        return arr
