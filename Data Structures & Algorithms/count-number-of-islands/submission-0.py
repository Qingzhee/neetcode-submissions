class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cur = 0
        def traverse(r, c):
            if r<0 or r>len(grid)-1 or c<0 or c>len(grid[0])-1 or grid[r][c] == "#":
                return
            if grid[r][c] == "1":
                grid[r][c] = "#"
                traverse(r-1, c)
                traverse(r+1, c)
                traverse(r, c+1)
                traverse(r, c-1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cur+=1
                    traverse(i,j)
        return cur
            