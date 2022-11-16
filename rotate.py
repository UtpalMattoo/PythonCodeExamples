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
        
        """
        method 1: works covers all use cases - run time exceeded
        for k in range(k):
          lst = []
          for j in range(len(nums)):
              if (j==0):
                lst.append(nums[j])
                nums[j] = nums[j-1]
              else:
                lst.append(nums[j])
                nums[j] = lst.pop(0)     
        """
        """ 
        method 2:
        for k in range(k):
            b = nums[:]
            for j in range(len(nums)):
                nums[j] = b[j-1]        
        """
        #method3
        print (nums)
        print (id(nums)) 

        if (k==0):
            return 

        if (k > len(nums)):
            for k in range(k):
                lst = []
                for j in range(len(nums)):
                    if (j==0):
                        lst.append(nums[j])
                        nums[j] = nums[j-1]
                    else:
                        lst.append(nums[j])
                        nums[j] = lst.pop(0)
        else: 
            if (len(nums)%2==0):
                for index, item in enumerate(nums[k:] + nums[0:k]):
                    nums[index] = item
            else:
                for index, item in enumerate(nums[k+1:] + nums[0:k+1]):
                    nums[index] = item

        print (nums)
        print (id(nums))
