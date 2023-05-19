
class Solution:
    
    def setZeroes(self, matrix):
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix) == 0 or matrix is None:
            print (f"bad input..exiting")
            return -1 #error code
        
        m = len(matrix)
        n = len(matrix[0])
        
        if not (1 <= m <= 200):
          raise ValueError("num of rows not 1 <= m <= 200")
          
        if not (1 <= n <= 200):
          raise ValueError("num of rows not 1 <= n <= 200")
          
        for row in range(len(matrix)):
            for col in range(0, row):
                if not (pow(-2, 31) <= matrix[row][col] <= pow(2, 31)-1):
                    raise ValueError("matrix element out of bounds")
                
        found = False
        
        for row_index, row in enumerate(matrix):
            
            if 0 in row:
                found = True
                #row_index = row_index
                break
        
        col_index = matrix[row_index].index(0)
        
        print (f"row = {row_index}; col = {col_index}")        
        print (f"Matrix input: {matrix}")

        if found == True:
            matrix[row_index][:] = [0] * len(row)               
            for i, row in enumerate(matrix[:][col_index]):
                matrix[i][col_index] = 0
        
        print (f"Matrix after setting cols to 0: {matrix}")    
        
matrix = [[1, 2, 3], [4, 0, 1], [7, 9, 9]]
Solution().setZeroes(matrix)          
