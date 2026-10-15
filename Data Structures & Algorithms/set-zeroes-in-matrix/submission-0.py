class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.append(r)
                    cols.append(c)
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for i in cols:
            for j in range(len(matrix)):
                matrix[j][i] = 0

        

            
        