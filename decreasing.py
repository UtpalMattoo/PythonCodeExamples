def decreasing(lst):
   
    if not lst:
        return -1
    
    if len(lst) == 0:
        return -1
    
    if len(lst) < 3:
        return -1
    
    c = lst[-1]
    stack = []
    stack.append(c)
    
    for index, val in enumerate(lst[-2::-1]):
        
        if val < stack[-1]:
            stack.append(val)
               
        while len(stack) > 0 and val >= stack[-1]:
            #print (f"popping {stack[-1]}")
            stack.pop()
        
        stack.append(val)            
        
        if len(stack) == 3:
            print (f"Elements in stack in decreasing order: {stack}")
            return True
        
    return False

#print (longestpalin([7,8,9,3,9,7,8]))
print (decreasing([1,2,3,4,5,6,2]))
