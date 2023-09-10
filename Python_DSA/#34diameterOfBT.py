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

def diameterOfBinaryTree(root) :
    # Your code goes here
    res = [0]
    
    def dob(root):
        if root == None:
            return -1
        left = dob(root.left)
        right = dob(root.right)
        res[0] = max(res[0], 2+left+right)
        
        return 1 + max(left, right)
    
    dob(root)
    return res[0]+1

root = treeInput()
printTreeDetail(root)
print(diameterOfBinaryTree(root))
