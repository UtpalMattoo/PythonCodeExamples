def reverse(nums, index, s_new):

    if (index == len(nums)-1):
        return s_new.append(nums[index])    
    elif (index < len(nums)-1):        
        reverse(nums, index+1, s_new)
    if len(s_new) > 0: #the last recursive call already entered 0th index in s_new
        s_new.append(nums[index])       
    return s_new
    
s = ["h","e","l","l","o"]
s_new = []
reverse (s, 0, s_new)
print (s_new)
