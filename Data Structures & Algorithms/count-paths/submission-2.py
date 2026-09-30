class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = []
        for i in range(m):
            arr.append([0] * n)

        for i in range(m):
            for j in range(n):
                if i == 0:
                    arr[i][j] = 1
                elif j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
        print(arr)
        return arr[m-1][n-1]