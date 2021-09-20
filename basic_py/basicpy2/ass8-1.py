class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if(self.root == None):
            self.root = newNode
            print("*",end="")
            return self.root
        

        ptr = self.root
        while(True):
            if(data < ptr.data): # go left
                
                if(ptr.left == None):
                    print("L",end="")
                    print("*",end="")
                    ptr.left = newNode
                    return self.root
                else:
                    ptr = ptr.left
                    print("L",end="")
            if(data >= ptr.data): # go right
                if(ptr.right == None):
                    print("R",end="")
                    print("*",end="")
                    ptr.right = newNode
                    return self.root
                else:
                    ptr = ptr.right
                    print("R",end="")
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
  

T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    root = T.insert(i)
    print()
