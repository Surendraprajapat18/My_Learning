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

#Problem in this code 
def sortedArrayToBST(sortArray):
    if len(sortArray)==0:
        return None
    
    m = len(sortArray)//2
    rootData = sortArray[m]
    root = BinaryTreeNode(rootData)
    sortArray[m]
    sortedArrayToBST(sortArray[:m])
    sortedArrayToBST(sortArray[m+1:])
    return root

sortArray = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(sortArray)
printTreeDetail(root)
    