def merge_intervals(lst):
        
    if not lst:
        print ("Empty list")
        raise ValueError("Empty list")
    
    #QA
    if not (1 <= len(lst) <= 10**4):
        print ("Invalid list length")
        raise ValueError("Invalid list length")
     
    #QA
    for i in lst:
        
        if type(i) != list:
            raise TypeError("Not all elements are lists")
                
        if len(i) != 2:
            raise ValueError("Not all elements are items of length 2")
        
        if i[0] > i[1]:
            raise ValueError("Invalid interval second value!")
        
        if  not (0 <= i[0] <= 10**4) or\
            not (0 <= i[1] <= 10**4) or\
            not (i[0] <= i[1]):
            raise ValueError("Invalid interval values!")
                
        if type(i[0]) != int or type(i[1]) != int:
            raise TypeError("Not all elements are integers")
        
    stack = []
    
    for index, val in enumerate(lst):
        if index == 0:
            stack.append(val[0])
            stack.append(val[1])            
        else:           
            if val[0] <= stack[-1]:
                stack.pop()
                stack.append(val[1])
            else:
                stack.append(val[0])
                stack.append(val[1])        
    
    print (stack)    
    
    #even elements in stack - return two adjacent elements as a list
    op=[]
    for index, val in enumerate(stack):
        if index % 2 == 0:
            op.append([stack[index], stack[index+1]])
    print (op)    
            
lst = [[1,2],[2,6],[6,10],[9,18]]    
merge_intervals(lst)
