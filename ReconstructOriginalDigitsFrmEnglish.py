class Solution(object):
    
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        from collections import Counter

        found = True
        lst = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]      
        for char in s:
            if char not in lst:
                found = False
                   
        if (found == False):
            raise ValueError("Input string has invalid characters.")
        
        if not (1 <= len(s) <= 100000):
           raise ValueError("Input out of bounds")
                
        
        op = ''        
        counter_dict = Counter(s)       
        stringNum_to_num = self.init_stringNum_to_num()
        
        while (max(counter_dict.values()) != 0): 
            
            for elem in stringNum_to_num: # move in ascending order
                
                found = True
                
                for char in elem: # order matters # this will just get only one occurance
                    if (char in s) and (found):
                        continue #found this char; go to next
                    else:
                        found = False
                
                if (found == True): #at least one 
                    op = op + str(stringNum_to_num[elem])
                    
                    for char in elem:
                        counter_dict[char] =  counter_dict[char] - 1
                        
        print (len(op))
        return (''.join(sorted(op)))
    
    def init_stringNum_to_num(self): 
        
        from collections import OrderedDict
        dict_stringNum_to_num = OrderedDict()
        
        dict_stringNum_to_num["zero"] = "0"
        dict_stringNum_to_num["one"] = "1"
        dict_stringNum_to_num["two"] = "2"
        dict_stringNum_to_num["three"] = "3"
        dict_stringNum_to_num["four"] = "4"
        dict_stringNum_to_num["five"] = "5"
        dict_stringNum_to_num["six"] = "6"
        dict_stringNum_to_num["seven"] = "7"
        dict_stringNum_to_num["eight"] = "8"
        dict_stringNum_to_num["nine"] = "9"
     
        return dict_stringNum_to_num
    
  
out = Solution().originalDigits("zerozerooneonethreetheretwo")  
print (out)

