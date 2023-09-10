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

#Function for printing the total number of nodes present in tree
def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1+leftCount+rightCount

#taking the input
root = treeInput()
#printing the detail of tree
printTreeDetail(root)
#printing the total number of nodes
print(numNodes(root))