
class checkInputs(object):
    
    def __init__(self, lst):
        self.lst = lst
        
    def doValidation(self):   
        len_err = False
        if not (0 <= len(self.lst) <= 1000000):
            len_err = True            
            #raise ValueError("lst can have at the most 10000 elements!")
    
        range_check = all( -1 * pow(10, 6) <= elem and elem <= (pow(10, 6)) for elem in self.lst)    

        #if not (range_check):
        #    raise ValueError("array elements out of bounds")    
        
        if not(range_check) or len_err:
            return False
        else:
            return True            
        
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next     

class Link_To_List(object):
    
    def __init__(self, lst, head):
          self.lst = lst
          self.head = head
               
    def  convert(self):
        for item in self.lst:
          if (self.head == None):
              self.head = ListNode(item)
              node = self.head
              node.val = self.head.val
              node.next = None
          else:
              new_node = ListNode(item) 
              node.next = new_node            
              node = node.next
        return self.head 


class arrange_List(object):
     
    def __init__(self, lst):
        self.lst = lst
        
    def build_list(self):
        if self.lst is None:
            raise ValueError ("list passed is empty")
            
        elif self.lst.next is None:
            return self.lst #One node list - return as is
        
        elif self.lst.next.next is None: 
            return self.lst #Two node list - return as is
        
        # List has minimum three nodes
        
        lo = self.build_odd()  #head of the odd-indexes list
                
        return lo
    
    def build_odd(self): #lst is the head of the odd index beginning
        
        #self.lst has 3 nodes or more   
        odd = self.lst
        even = odd.next
        even_head = even
        
        while even is not None and even.next is not None: 
            # this validation was already done
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return self.lst
    
l1 = [1,2,3,4,5,10000,6]

lst_obj = checkInputs(l1)

if not lst_obj.doValidation():
    print ("exiting...")
    raise ValueError("Range Error or list length error")
    
head = None
init_Link_To_List = Link_To_List(l1, head)
lnkd_l1 = init_Link_To_List.convert() #to LL

curr = lnkd_l1

print ("\nInput list:")
while curr is not None:
    print (f"{curr.val}")
    curr = curr.next

modifier_class = arrange_List(lnkd_l1)

rearr_list = modifier_class.build_list()

print ("\nOutput list:")
while rearr_list is not None:
    print (rearr_list.val)
    rearr_list = rearr_list.next
