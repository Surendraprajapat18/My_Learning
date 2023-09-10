import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
#Function for printing the detailed of Tree
def printTreeDetail(root):
    if root == None:
        return 
    print(root.data, end = " : ")
    if root.left != None:
        print("L", root.left.data, end = ",")
    if root.right != None:
        print("R", root.right.data, end="")
    print()
    printTreeDetail(root.left)
    printTreeDetail(root.right)

#Function for finding the min value from right and left
def minTree(root):
    if root == None:
        return 1000000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)

#Function for finding the max value from right and left
def maxTree(root):
    if root == None:
        return -1000000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return min(leftMax, rightMax, root.data)
    
#Function for find the given Tree is BST or Not
def isBST1(root):
    if root == None:
        return True
    
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if root.data > rightMin or root.data <= leftMax:
        return False

    isLeftBST = isBST1(root.left)
    isRightBST = isBST1(root.right)
    return isLeftBST and isRightBST

'''
Function for check tree is BST or Not This BST2 function decreses 
time complexity From BST1 function
'''
def isBST2(root):
    if root == None:
        return 100000, -100000, True
    
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    isTreeBST = True
    if root.data <= leftMax or root.data >rightMin:
        isTreeBST = False
    if not(isLeftBST) or not(isLeftBST):
        isTreeBST = False

    return minimum, maximum, isTreeBST

#Func 3 for BST cheacking
def isBST3(root, min_range, max_range):
    if root == None:
        return True
    
    if root.data < min_range or root.data > max_range:
        return False
    
    isLeftWithinConstraints = isBST3(root.left, min_range, root.data-1)
    isRightWithinConstraints = isBST3(root.right, root.data, max_range)

    return isLeftWithinConstraints and isRightWithinConstraints

#Function for the taking input levelwise
def levelWiseTreeInput():
    q = queue.Queue()
    print("Enter root:")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node = q.get()
        print("Enter left child of ", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        print("Enter right child of ", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root
    

root = levelWiseTreeInput()
printTreeDetail(root)
print(isBST3(root, -10000, 10000))



'''
                    4
                 /     \
                2       6
              /   \   /   \
             1    30 5     7
'''