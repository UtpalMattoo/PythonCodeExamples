# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes 
# contains a single digit. Add the two numbers and return the sum as a linked list.
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:00:36 2021

@author: Utpal
"""

# Definition for singly-linked list.

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
       
class Solution(object):
    
    # def __init__(self, l1, l2):
    #       self.l1 = l1
    #       self.l2 = l2
          
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
       
        #check for either or both lists for null list condition:
        if (l1 == None and l2 == None):
            return ValueError("Error. Both lists are null")
        elif (l1 == None):
             return rev_list(lst_to_str(l2))
        elif (l2 == None):
             return rev_list(lst_to_str(l1))
        else:            
            num1 = lst_to_str(l1)
            num2 = lst_to_str(l2)         
            return rev_list(num1 + num2)

def lst_to_str(lnkdLst):
    test_str = ""
    while (lnkdLst != None):
       test_str = test_str + str(lnkdLst.val)
       lnkdLst = lnkdLst.next
    return int(test_str[::-1])   

def rev_list(rslt):
    su = str(rslt)
    su = su[::-1]
    head = None
    for c in su:
        if (head == None):
            head = ListNode(c)
            node = head
            node.val = head.val
            node.next = None
        else:
            new_node = ListNode(c)
            node.next = new_node            
            node = node.next
    return head
   
l1 = [2,4,3]
l2 = [5,6,4]

head = None
init_Link_To_List = Link_To_List(l1, head)
lnkd_l1 = init_Link_To_List.convert() #to LL

init_Link_To_List = Link_To_List(l2, head)
lnkd_l2 = init_Link_To_List.convert() #to LL

# sol_obj = Solution(lnkd_l1, lnkd_l2)   
su = Solution().addTwoNumbers(lnkd_l1, lnkd_l2)
print (su.val)
