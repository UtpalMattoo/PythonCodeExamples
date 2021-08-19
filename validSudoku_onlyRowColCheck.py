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
        
        print (f"row check = {row_bool}; col check = {col_bool}")
        return (row_bool and col_bool)
    
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
        
board = np.array([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

isValid = Solution().isValidSudoku(board)
print (isValid)

"""
Comment:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
