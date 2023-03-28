# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:39:21 2023
least complicated version I could come up with so far
@author: utpal
"""

class Solution(object):
    
    def __init__(self, s):
        self.strseq = s
    
    def findLongestSubString(self, strseq):
       
       lst = []
       
       if len(strseq) == 0:
           return -1
       
       if len(strseq) == 1:
           return 1

       for index, val in enumerate(strseq):
           
           inLst = []
           inLst.append(val)

           for i, char in enumerate(strseq[index+1:]):
               if char in inLst: 
                   lst.append(inLst)               
                   break
               else:
                   inLst.append(char)  
           
           if inLst not in lst:
               lst.append(inLst)
           
           
       if (index+1 == len(strseq)): 
               lst.append(list(strseq[-1]))
           
       max_len = 0
       for item in lst:
           if len(item) > max_len:
               max_len = len(item)
           
       return max_len, lst
                
  
s = "bbbbbxcv"
#s = "abcabc"
#s = "pwwkec"
x = Solution(s)
max_len, new_lst = x.findLongestSubString(s)
print (f"Longest unique substring is: {max_len};\
         \nAll combinations tried for max length are:\n {new_lst}")
    
