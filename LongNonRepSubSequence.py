# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:51:47 2021

@author: Utpal
"""

class Solution(object):
    
    # def __init__(self, s):
    #     self.s = s
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        new_lst = []
        for char in s:
            found_char, lst = self.found (char, lst)                                                           
            new_lst.append(lst)
        return new_lst
    
    def found (self, char, lst):
        new_lst = []
        found_char = False
        
        if not lst:
            new_lst.append(char)
            return found_char, new_lst
        else: 
            for item in lst:    
              if ((char in item) and (item[-1] != 'X')):
                  found_char = True
                  item = item + 'X'                  
                  new_lst.append(item)
                  if char not in new_lst:
                      new_lst.append(char)
              elif ((char not in item) and (item[-1] != 'X')):
                  new_lst.append(item+char)
                  if char not in new_lst:
                      new_lst.append(char)                  
            return found_char, new_lst 

# s = "abbbb"
# s = "abbac"
# s = "pwwkec"
s = "aaxbcdcdax"          

new_lst = Solution().lengthOfLongestSubstring(s)
from collections import defaultdict
d = defaultdict(lambda: 0)

for elem in new_lst:
   for item in elem:
      if (item[-1] == 'X'):
        d[item[-1]] = len(item[-1]) -1    
      else:
        d[item]  = len(item)

print (d.values())
print (d.keys())
val = max(d.values())
print (val)
