def find_long_substr(inp_str):
    
    lst = []    
    
    for outer_index, val in enumerate(inp_str):
        
        temp = ''
        inner_index =  outer_index
        val = ''

        for i, val in enumerate(inp_str[inner_index:]):  
           
            if val not in temp:   
                temp = temp + val                   
            else:
                 break
        
        if (i == len(inp_str)-1): #you reached the end of the string
            lst.append(temp)
            return lst
        else: # val was in temp
            lst.append(temp)
    
    return lst, len(max(lst, key=len)), max(lst, key=len)
            
#arr ='abcdefghuuuuioprtyhjkl'
#arr = "aaxbcdcdax"  
#arr = 'aaxbcdcdax'
arr = 'peewcwwkec'
lst, max_len, long_str = find_long_substr(arr)

print (lst)
print (max_len)
print (long_str)
