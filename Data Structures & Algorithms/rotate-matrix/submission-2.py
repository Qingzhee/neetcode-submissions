class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mid = len(matrix)//2
        n = len(matrix)
        for i in range(mid):
            holder = matrix[i].copy()
            matrix[i] = matrix[n-1-i] 
            matrix[n-1-i] = holder
        start = 1
        for i in range(n):
            for j in range(start,n):
                holder = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = holder
            start+=1



