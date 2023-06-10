# credit: https://www.geeksforgeeks.org/level-order-tree-traversal/ 
# above code was modfied slightly to make it more intuitive

class TreeNode:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    print (f"the height of the tree is {h}")
    print (list(range(1,h+1)))
    for i in range(1, h+1):
        print (f"\ncalling printcurrlevel with LEVEL value = {i}")
        printCurrentLevel(root, i, 1) # third parm always starts at 1
 
# Print nodes at a current level
def printCurrentLevel(root, level, curr):
    if root is None:
        return
    #print (level)
    #if level == 1:
    if curr == level:
        print(root.data, end=".... ")
    elif curr < level:
        #print (f"result after recursion = {level}")
        #printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.left, level, curr + 1)
        #printCurrentLevel(root.right, level-1)
        printCurrentLevel(root.right, level, curr + 1)
 
""" 
    Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
 
def height(node):
    if node is None:
        return 0
    
    # Compute the height of each subtree
    #lheight = height(node.left)
    lheight = 1 + height(node.left)
    #rheight = height(node.right)
    rheight = 1 + height(node.right)
 
    # Use the larger one
    if lheight > rheight:
       #return lheight+1
       return lheight
    else:
       #return rheight+1
       return rheight
 
# Driver program to test above function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(7)
root.right.right.left = TreeNode(71)
 
print("Height is -")
printLevelOrder(root)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
