
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
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

def largestData(root, n):
    ans = 0
    if root == None:
        return -1
    leftLarget = largestData(root.left, n)
    rightLarget = largestData(root.right, n)
    if leftLarget<n or rightLarget<n or root.data<n:
        ans += 1
   
    
    #largest = max(leftLarget, rightLarget, root.data)
    return ans


root = treeInput()
n = int(input("N: "))
printTreeDetail(root)
print("largestElement:",largestData(root, n))

