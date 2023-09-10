#class for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
#Function for print the tree detailed
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

#Function for taking input
def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

#Function for printing the sum of all binary tree value sum
def sumNodes(root):
    if root == None:
        return 0
    leftCount = sumNodes(root.left)
    rightCount = sumNodes(root.right)
    return leftCount + rightCount + root.data


root = treeInput()
printTreeDetail(root)
print(sumNodes(root))