from sympy import O


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

def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh-rh) > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isrightBalanced = isBalanced(root.right)
    if isrightBalanced and isLeftBalanced:
        return True
    else:
        return False

root = treeInput()
printTreeDetail(root)
print(isBalanced(root))
