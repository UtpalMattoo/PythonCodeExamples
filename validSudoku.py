# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:52:05 2021
@author: Utpal
WIP..
"""

import numpy as np

class Solution(object):
        
    def checkValidBox(self, lst): # for all rows, cols and sub-boxes
        
        #dup and range check
        isValid = True       
        
        for elem in lst:        
            if set(elem) == elem and self.inValidRange(elem):
                continue
            else: 
                isValid = False
                break #don't go further; will lose info on what was false
                
        return isValid
    
    def inValidRange(self, lst, low=0, high=10): #range will check 0 to 9
        inRange = all(i in range(low, high) for i in lst)
        return inRange
    
    def getAllSubboxes(self, num_of_subBoxes, shape_per_subBox, offset):
                
        # board_rows = list(range(0, num_of_subBoxes))
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
        print (sub_box_dims)  
             
        rows = []
        for sub_box in sub_box_dims:
            #print ("************")
            #print (sub_box)
            sub_box_indices_lst = list(itertools.product(*sub_box))
            #print (sub_box_indices_lst)
            lst = []
            for loc_in_subbox, indices in enumerate(sub_box_indices_lst):
                #print (f"indices = {indices}; type(indices)")
                i = indices[0]
                j = indices[1]
                #print (f"i={i}; j = {j}")
                if (board[i][j] != '.'):
                    lst.append(board[i][j])
            rows.append(lst)
        print (rows)
        
        #rows contains all items from each sub-box
        #call check valid sub-box for each element (list) in "rows" to check for 
        #sub-box validity
                
        return 
                 
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
        print (rows)
        row_bool = self.checkValidBox(rows) #one boolean for all rows in board
        
        #2. Col check
        cols = []
        for col in range(np.shape(board)[1]):
            lst = []
            for item in list(board[:,col]):
                if (item != '.'):
                    lst.append(item)
            cols.append(lst)
        print (cols)
        col_bool = self.checkValidBox(cols) #one boolean for all cols in board
        
        #3. Sub-box check
        sub_box_lst = []
        num_of_subBoxes = 9
        shape_per_subBox = (3,3)
        offset = 3
        sub_box_lst = self.getAllSubboxes(num_of_subBoxes, shape_per_subBox, offset)
    
board = np.array(
[["5","3",".",".","7",".",".",".","."]
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

# [[[0:2], [0:2]] , [[3:5], [3:5]], [[6:8], [6:8]].........]
