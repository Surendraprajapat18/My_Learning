class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

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

#Printing the leaf nodes from tree
def numLeafNodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    numLeafleft = numLeafNodes(root.left)
    numLeafright = numLeafNodes(root.right)
    return numLeafleft + numLeafright

#Printing the k node from tree
def printDepthk(root, k):
    if root == None:
        return 
    if k == 0:
        print(root.data)
        return 
    printDepthk(root.left, k-1)
    printDepthk(root.right, k-1)

def printDepthkV2(root, k, d=0):
    if root == None:
        return 
    if k == d:
        print(root.data)
        return 
    printDepthkV2(root.left, k, d+1)
    printDepthkV2(root.right, k, d+1)



root = treeInput()
printTreeDetail(root)
#print("Number of Leaf Nodes:", numLeafNodes(root))
#print(printDepthkV2(root, 2))
print(numLeafNodes(root))
