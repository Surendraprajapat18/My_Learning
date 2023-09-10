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

def rootToLeafPath(root, s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l
    
    leftOutput = rootToLeafPath(root.left, s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput

    rightOutput = rootToLeafPath(root.right, s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput

    else:
        return None

root = levelWiseTreeInput()
printTreeDetail(root)
print(rootToLeafPath(root, 10))

