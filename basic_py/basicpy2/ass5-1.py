class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        if self.isEmpty():
            return "List is empty"
        else:
            s = 'link list : '
            current = self.head
            while current.next is not None:
                s += str(current.data) + '->'
                current = current.next
            s += str(current.data)
            return s

    def append(self, data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
            self.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            self.size += 1

    def insert(self, index, data):
        if 0 <= index <= self.size:
            if self.head is None or index == self.size:
                self.append(data)
            elif index == 0:
                current = self.head
                self.head = self.Node(data)
                self.head.next = current
            else:
                current = self.head
                for i in range(index-1):
                    current = current.next
                p = self.Node(data)
                p.next = current.next
                current.next = p
            print("index = " + str(index) + " and data = " + str(data))
            self.size += 1
        else:
            print("Data cannot be added")
        

n=input("Enter Input : ").split(',')
it=LinkedList()
for i in n[0].split():
    it.append(i)
for i in range(1,len(n)):
    s = n[i].strip().split(':')
    print(it)
    it.insert(int(s[0]),s[1])
print(it)
