# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not (2 <= len(nums) <= 1000):
            return -1
        else:
            print ("num check passed")
        
        if not (pow(-10,9) <= target <= pow(10,9)):
            return -1
        else:
            print ("target check passed")
        
        for index, val in enumerate(nums):
            print (index)
            if not (pow(-10, 9) <= nums[index] <= pow(10, 9)):
                print ("Invalid value found in nums: {}".format(nums[index]))
                return -1
            else:
                continue
        
        lst = []            
        found = False
        
        for index1, val1 in enumerate(nums):  
            if (found == False):
                lst = []  
                lst.append(index1)
                if (found==False):
                   for index2, val2 in enumerate(nums):
                        if index2 != index1:
                            if ((val1 + val2) == target):
                                print ("val1: {}; val2: {}".format(val1, val2))
                                found = True
                                lst.append(index2)
        
        return lst
    

test_class = Solution()
nums = [2,7,11,15]
target = 9
val = test_class.twoSum(nums, target)
print (val)
