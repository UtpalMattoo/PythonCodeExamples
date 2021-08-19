# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:10:11 2021

@author: Utpal
"""


class Node(object):
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        
class LL():
    def __init__(self, head):
        self.head = head
        
    def deleteNode(self, head, index):
        
        if (head is None):
            return "Error: cant delete from empty list"
                
        i = 1 # count at current node
        
        if (index ==1): #delete head
            head = head.next
        else: 
            prev = head
            curr = head
            
            while (curr.next is not None):
                prev = curr
                curr = curr.next
                i+=1
            
                if (i == index) and (curr.next is None):
                    prev.next = None
                elif (i==index) and (curr.next is not None):
                    prev.next = curr.next
        
        return head
    
# assume index is always less than the length of the list    
head = Node(7)
head.next = Node(10)
head.next.next = Node (20)
head.next.next.next = Node(50)
# head.next.next.next.next = None
# 7 --> 10 ---> 20 ---> 50

curr = head
while (curr != None):
    print (curr.val)
    curr = curr.next
    
llclass = LL(head)
head = llclass.deleteNode(head, 1)

curr = head
while (curr != None):
    print (curr.val)
    curr = curr.next
    
head = None
