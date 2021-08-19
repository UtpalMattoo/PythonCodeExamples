# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:06:03 2021

@author: Utpal
"""

import numpy as np

class Solution(object):
        
    def checkValidBox(self, lst): # for all rows, cols and sub-boxes
        
        #dup and range check
        isValid = True       
        
        for elem in lst:  
            # print (elem)
            if sorted(set(elem)) == sorted(elem) and self.inValidRange(elem):
                continue
            else: 
                isValid = False
                break #don't go further; will lose info on what was false
                 
        return isValid
    
    
    def inValidRange(self, lst, low=1, high=9): #range will check 1 to 9
        inRange = all(True if 0 <= int(item) <= 9 else False for item in lst)
        # print (f"lst = {lst};;;; inRangeResult = {inRange}")
        return inRange
    
    
    def getAllSubboxes(self, num_of_subBoxes, shape_per_subBox, offset):
                
        import itertools
        
        l1 = list(range(0, offset))
        l2 = list(range(offset, 2*offset))
        l3 = list(range(2*offset, 3*offset))
                
        all_list = [l1, l2, l3]
        sub_box_dims = []
        lst = []
        for elem1 in all_list:
           for elem2 in all_list:
              lst.append(elem1)
              lst.append(elem2)
              sub_box_dims.append(lst)
              lst = []
        # print (sub_box_dims)  
             
        subBox_elements = []
        for sub_box in sub_box_dims:
            sub_box_indices_lst = list(itertools.product(*sub_box))
            # print (sub_box_indices_lst)
            lst = []
            for loc_in_subbox, indices in enumerate(sub_box_indices_lst):
                i = indices[0]
                j = indices[1]
                if (board[i][j] != '.'):
                    lst.append(board[i][j])
            subBox_elements.append(lst)
        
        return subBox_elements
    
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #1. Row check
        rows = []
        for row in range(np.shape(board)[0]):
           lst = []
           for item in list(board[row,:]):
               if (item != '.'):
                   lst.append(item)
           rows.append(lst)           
        # print ("Rows as lists::")
        # print (rows)
        row_bool = self.checkValidBox(rows) #one boolean for all rows in board
    
        #2. Col check
        cols = []
        for col in range(np.shape(board)[1]):
            lst = []
            for item in list(board[:,col]):
                if (item != '.'):
                    lst.append(item)
            cols.append(lst)
        # print ("Columns as lists::")
        # print (cols)
        col_bool = self.checkValidBox(cols) #one boolean for all cols in board
        
        #3. Sub-box check
        num_of_subBoxes = 9
        shape_per_subBox = (3,3)
        offset = 3
        sub_box_element_lst = self.getAllSubboxes(num_of_subBoxes, shape_per_subBox, offset) 
        subBox_bool = self.checkValidBox(sub_box_element_lst) #one boolean for all elements in all sub-boxes

        print (f"row check = {row_bool}; col check = {col_bool}; sub_box_check = {subBox_bool}")
        return (row_bool and col_bool and subBox_bool)
       
board = np.array([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
# False


isValid = Solution().isValidSudoku(board)
print (isValid)      

# the board above and below are same - replace the 8 at (0,0) by 5 or vice-versa

# board = np.array(
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]])
# ## True       

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
