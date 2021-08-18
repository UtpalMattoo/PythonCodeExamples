def reverse(nums):

    if (len(nums) == 1):
        return nums[-1]    
    else:
        return reverse(nums[-1]) + reverse(nums[0:len(nums)-1])
    
# s[i] is a printable ascii character       
s = ["a","b"]
snew = list(reverse (s))
print (snew)
