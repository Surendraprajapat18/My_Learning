class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Map:

    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
    
    def size(self):
        return self.count
    
    def getBucketIndex(self, hc):
        return (abs(hc)%(self.bucketSize))
    
    def getValue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]

        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        
        return None

    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return head.value

            prev = head
            head = head.next
        return None

    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2*self.bucketSize
        self.count = 0
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next

    def loadFactor(self):
        return self.count/self.bucketSize
   
    def insert(self, key, value):

        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()


m = Map()
for i in range(10):
    m.insert('abc' + str(i), i+1)
    print(m.loadFactor())

for i in range(10):
    print('abc' + str(i)+':' , m.getValue('abc'+str(i)))

# m.insert('Surendra', 2)
# print(m.size())
# m.insert("Vijay", 3)
# print(m.size())
# m.insert("Arpit", 4)
# print(m.size())
# print(m.getValue("Arpit"))
# print(m.getValue("Surendra"))
# m.remove("Arpit")
# print(m.getValue("Arpit"))
# print(m.getValue("Surendra"))
# print(m.size())

