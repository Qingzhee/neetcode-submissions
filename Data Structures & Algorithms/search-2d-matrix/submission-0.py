class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        front_row = 0
        back_row = len(matrix)-1
        y = len(matrix[0])-1
        row_found = False
        while front_row <= back_row:
            mid_row = (front_row + back_row) //2
            #print(mid_row)
            #print(matrix[mid_row][y])
            #print(matrix[mid_row][0])
            if target <= matrix[mid_row][y] and target >= matrix[mid_row][0]:
                row_found = True
                break
            if matrix[mid_row][0]<target:
                front_row = mid_row+1
            else:
                back_row = mid_row-1
            
        if row_found == False:
            return False

        front_col = 0
        back_col = len(matrix[0])-1

        while front_col<=back_col:
            mid_col = (front_col+back_col)//2
            if matrix[mid_row][mid_col] == target:
                return True
            if matrix[mid_row][mid_col] < target:
                front_col = mid_col+1
            else:
                back_col = mid_col -1

        return False



