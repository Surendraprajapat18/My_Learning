import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

#LevelWise input 
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

#Print tree detailed levelwise
def printDetailedLvlWise(root):
   l = []
   if root == None:
       return l
   queue = []
   queue.append(root)
   while len(queue)>0:
       curr = BinaryTreeNode(queue[0].data)
       Node = queue.pop(0)
       l.append(curr.data)
       if Node.left != None:
           queue.append(Node.left)
       if Node.right != None:
           queue.append(Node.right)
            
   return l

root = levelWiseTreeInput()
ans = printDetailedLvlWise(root)
print(*ans)