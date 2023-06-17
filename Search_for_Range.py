"""
usage:
    find_range([1,1,1,2],2)
    find_range([1,3,3,3,4],3) 
    find_range([1,1,1,2,4,4],4) 
    find_range([1,1,1,1,1,1],1) 
    find_range([1,3,4],4) 
"""
   
def find_range(lst, target):
    
    
    """
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
    """
    
    if len(lst) > 105:
        raise ValueError("Length > 105")
    
    rangecheck = all( elem >= 0 and elem <= 109 for elem in lst)
    
    if not rangecheck:
        raise ValueError("element value out of bounds")
        
    min = lst[0]
    nondec = True
    for item in range(1, len(lst)):
        if lst[item] >= min:
            min = lst[item]
            continue
        else:
            nondec = False
            break
    
    if nondec == False:
        raise ValueError("Error not non Dec")
        
    if target > 109 or target < -109:
        raise ValueError("Target is out of bounds")
        
    left, right = bin_search(lst, target, 0, len(lst)-1, False)

    print ([left, right])
    
def bin_search(lst, target, left, right, to_print=False):
             
    if len(lst) == 0:
        return 
    
    if to_print:
        print (f"left = {left}; right = {right}; lst = {lst};")
    
    mid = left+right//2
    if to_print:
        print (f"mid={mid}")
    
    if target == lst[mid]:
        
        left = right = mid
        
        #get left end
        while left > 0 and lst[left-1] == target:
            left -=1           
            
        #get right end
        while right < len(lst)-1 and lst[right+1] == target:
            right +=1           
       
        if to_print:
            print (f"Inner: {[left,right]}")
            
        return left, right
    
    if target < lst[mid]:
        return bin_search(lst, target, left, mid-1)
                      

    if target > lst[mid]:
        return bin_search(lst, target, mid, right) 
                 
    return left, right   
