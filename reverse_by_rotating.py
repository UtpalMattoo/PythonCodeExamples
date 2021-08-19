
def reverse_by_rotating(nums):

    # if not( 0 <= k <= 105):
    #     assert pow(10, 0) <= k <= pow(10, 5), "k is outside valid range"
  
    if not( 1 <= len(nums) <= 105):
        assert pow(10, 0) <= len(nums) <= pow(10, 5), "k is outside valid range"      
        
    # range_check = all( pow(-2, 31) <= elem and elem <= pow(2, 31) for elem in nums)
  
    # if not (range_check):
    #     raise ValueError("array elements out of bounds") 
    
    for k in range(0, len(nums)):
      lst = []
      for j in range(k, len(nums)):
          if (j==k):  
              lst.append(nums[j])
              nums[j] = nums[-1]
          else:
              lst.append(nums[j])
              nums[j] = lst.pop(0)
    return nums

s = ['a','b','c','d',1,2,3,10,90]
s_new = reverse_by_rotating (s)
print (s_new)
