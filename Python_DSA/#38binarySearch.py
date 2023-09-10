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

#function for searching the value x in tree if it is present so return True else false
def search(root, x):
    if root == None:
        return False
    elif root.data == x:
        return True
    elif root.data < x:
        return search(root.right, x)
    else:
        return search(root.left, x)

#Function for taling input levelwise
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
print(search(root, 5))




