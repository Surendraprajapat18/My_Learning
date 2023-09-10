import queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printTree(root):
    # Not a base case but an edge case
    if root == None:
        return 
        
    print(root.data)
    for child in root.children:
        printTree(child)

# Function for printing the tree detailed
def printTreeDetailed (root):
    if root == None:
        return 

    print(root.data, ": " ,end = "")
    
    for child in root.children:
        print(child.data, ",", end = "")
    print()
    
    for child in root.children:
        printTreeDetailed(child)

# Function for taking input
def takeTreeInput():
    print("Enter root Data")
    rootData = int(input())
    # Not a base case but an edge case
    if rootData == -1:
        return None
    
    root = TreeNode(rootData)

    print("Enter number of children for ", rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root

def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node = q.get()
        print("Enter num of children for ", current_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print("Enter next child for ", current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root


# Function for Counting Node
def numNodes(root):
    if root == None:
        return 0
    
    count = 1
    for child in root.children:
        count = count + numNodes(child)
    return count

# Function for Sum of All Nodes value
def sumNodes(root):
    if root == None:
        return 0
    
    sumofnodes = root.data
    for child in root.children:
        sumofnodes = sumofnodes + sumNodes(child)
    return sumofnodes

# Function for Counting Node
def largestData(root):
    if root == None:
        return 0
    
    largestelement = root.data
    for child in root.children:
        largestelement = max(largestelement, largestData(child))
    return largestelement




root = takeTreeInputLevelWise()
printTreeDetailed(root)
print(numNodes(root))
#print(largestData(root))

