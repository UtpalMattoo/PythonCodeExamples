### Version 1 (should use less space than Version 2 below - uses a Python list as a queue to store 2 temp values)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if not( 0 <= k <= pow(10, 5)):
            assert 0 <= k <= pow(10, 5), "k is outside valid range"
            
        if not( pow(10, 0) <= len(nums) <= pow(10, 5)):
            assert pow(10, 0) <= len(nums) <= pow(10, 5), "num length is outside valid range"
        
        range_check = all( pow(-2, 31) <= elem and elem <= (pow(2, 31)-1) for elem in nums)
        
        if not (range_check):
            raise ValueError("array elements out of bounds")
        
        for k in range(k):
          lst = []
          for j in range(len(nums)):
              if (j==0):
                lst.append(nums[j])
                nums[j] = nums[j-1]
              else:
                lst.append(nums[j])
                nums[j] = lst.pop(0)  
        return nums

s = [-1,-100,3,99]
s_new = rotate (s,2)
print (s_new)

### Version 2

def rotate(nums, k):

    if not( 0 <= k <= 105):
        assert pow(10, 0) <= k <= pow(10, 5), "k is outside valid range"
  
    if not( 1 <= len(nums) <= 105):
        assert pow(10, 0) <= len(nums) <= pow(10, 5), "k is outside valid range"      
        
    range_check = all( pow(-2, 31) <= elem and elem <= pow(2, 31) for elem in nums)
  
    if not (range_check):
        raise ValueError("array elements out of bounds") 
  
    for k in range(k):
        b = nums[:]
        for j in range(len(nums)):
            nums[j] = b[j-1]    
            
    return nums

s = [1,2,3,4,5,6,7]
s_new = rotate (s,3)
print (s_new)
