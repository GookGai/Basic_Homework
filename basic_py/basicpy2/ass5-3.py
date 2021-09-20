class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        s = ""
        current = self.head
        while current.next:
            s += str(current.data) + " "
            current = current.next
        s += str(current.data)
        return s

    def reverse(self):
        s = ""
        current = self.tail
        while current.prev:
            s += str(current.data) + " "
            current = current.prev
        s += str(current.data)
        return s

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.size += 1

a = input("Enter Input (L1,L2) : ").split()
Wlist1 = a[0].split("->")
Wlist2 = a[1].split("->")

print("L1    :"," ".join(Wlist1))
print("L2    :"," ".join(Wlist2))
ansl1 = DLinkedlist()
ansl2 = DLinkedlist()

for i in Wlist1:
    ansl1.append(i)
for j in Wlist2:
    ansl2.append(j)
print("Merge :" , ansl1 , ansl2.reverse())