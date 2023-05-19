# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:19:52 2021

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
        from collections import defaultdict
        import string
        lst = []
        new_lst = []
                
        if not (0 <= len(s) <= 50000):
           raise ValueError("Input out of bounds")
        if s == "":
           return 0
            
        for char in s:
            found_char, lst = self.found (char, lst)                                                          
            new_lst.append(lst)
        #print (new_lst)    
        d = defaultdict(lambda: 0)
        for elem in new_lst:
            for item in elem:
              if (item[-1] == 'X'):
                d[item[-1]] = len(item[-1]) -1    
              else:
                d[item]  = len(item)
        #print (d.values())
        
        #qucik fix to test
        lst1 = [ (key, val) for key, val in d.items()]
        #print (lst1)
        max_init = 0        
        long_str = ''        
        for item in lst1:
            if item[1] > max_init:
                max_init = item[1]
                long_str = item[0]            
        print (f" long_str = {long_str}, max_len = {max_init}")
        
        val = max(d.values())
        return val

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

#s = "abbbb"
#s = "abbac"
s = "peewcwwkec"
#s = "aaxbcdcdaxjlijliewleuwieuuvs;pwq"  
subseq_len = Solution().lengthOfLongestSubstring(s)
print (subseq_len)
