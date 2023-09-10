class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def printTreeDetail(root):
    if root == None:
        return 
    print(root.data)
    if root.left != None:
        print(root.left.data)
    if root.right != None:
        print(root.right.data)
    print()
    printTreeDetail(root.left)
    printTreeDetail(root.right)

#post_order Traverses
def printTreePostOrder(root):
    if root == None:
        return 
    
    printTreeDetail(root.left)
    printTreeDetail(root.right)
    print(root.data)

#in_order Traverses
def printTreeDetailInOrder(root):
    if root == None:
        return 
    
    if root.left != None:
        print(root.left.data)
    print(root.data)
    if root.right != None:
        print(root.right.data)
    
    printTreeDetail(root.left)
    #print(root.data)
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




root = treeInput()
#printTreeDetail(root)
#print()

printTreePostOrder(root)
print()
