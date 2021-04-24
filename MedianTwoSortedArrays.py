# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:05:53 2021

@author: Utpal
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if (nums1 is None) and (nums2 is None):
            raise ValueError("Both lists are null. Returning.")
            
        if not (0 <= len(nums1) <= 1000):
            raise ValueError("nums1 out of bounds len > 1000")
            
        if not (0 <= len(nums2) <= 1000):
            raise ValueError("nums2 out of bounds len > 1000")
            
        if not (1 <= len(nums1 + nums2) <= 2000):
            raise ValueError("nums1+nums2 out of bounds > 2000")
                              
        if (nums1 is None):
            return nums2
        
        if (nums2 is None):
            return nums1
            
        nums = [nums1, nums2]
        
        tot_len = len(nums1) + len(nums2)
        
        num = [0] * tot_len

        elemValCheck = self.checkElement(nums)
        
        if (elemValCheck == -1):           
            raise ValueError("element length out of bounds")
            
        i = j = k = 0
        
        try:
            
            while i <= len(nums1) - 1 or j <= len(nums2) - 1:
                
                if  (nums1[i] < nums2[j]) and (i <= len(nums1)-1 and j <= len(nums2) -1):
                    num[k] = nums1[i]
                    i +=1
                    
                elif (nums2[j] < nums1[i]) and (j <= len(nums2) - 1 and i <= len(nums1) -1):
                    num[k] = nums2[j]
                    j +=1
                    
                elif (nums1[i] == nums2[j]) and (i <= len(nums1) -1 or j <= len(nums2) -1):
                    num[k] = nums2[j]
                    k +=1
                    num[k] = nums1[i]
                    i +=1
                    j +=1                    
                k +=1   
                
        except IndexError: #side effect of incrementing index in the if blocks above
            
            if (j == len(nums2)):
                while (i <= len(nums1)-1):
                    num[k] = nums1[i]
                    i +=1
                    k +=1
        
            if (i == len(nums1)):
                while (j <= len(nums2)-1):
                    num[k] = nums2[j]
                    j +=1
                    k +=1
      
        if len(num) % 2 == 0:
            q = len(num)//2
            a = float(num[q-1])
            b = float(num[q])
            median = (a+b)/2
        else: 
            q = len(num)//2
            median = num[q]                      
        return median #could also return num
        
    def checkElement(self, nums):
        for num in nums:
          for elem in num:
            if (-10 **6 <= elem <= 10 **6):
                 continue                
            else:
                return -1        
        return 0
        
nums1 = [1, 2]
nums2 = [3, 4]

retVal = Solution().findMedianSortedArrays(nums1, nums2)
print (retVal)
