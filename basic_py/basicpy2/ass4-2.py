class Queue:
    
    class Node:

        def __init__(self,value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.last = None
        self.first = None
        

    def insert(self,value):
        newNode = self.Node(value)
        if(self.first == None):
            self.first = newNode
            self.last = newNode
        else : 
            self.last.next = newNode
            newNode.prev = self.last
            self.last = newNode
          

    def pop(self):
        if(self.first != None):
            value = self.first.value
            self.first = self.first.next
            if(self.first != None):
                self.first.prev = None

            if(self.first == None):
                self.last = None
        else:
            return False
        return value
    

    def head(self):
        if(self.first != None):
            return self.first.value

    def tail(self):
        return self.last.value

    def empty(self):
        return True if self.first == None else False

    def print(self):
        lst = []
        last = self.first
        while (last != None):
            # print(last.value,end=", ")
            lst.append(last.value)
            last = last.next
        return lst
q = Queue()

x = input("Enter Input : ").split(',')

 
def ES(que,value):
    if(que.empty()):
        que.insert(["ES",value])
    else:
        nQ = Queue()
        while(not que.empty() and que.head()[0] == "ES"):
            nQ.insert(que.pop())
        nQ.insert(["ES",value])
        while(not que.empty()):
            nQ.insert(que.pop())
        return nQ
    return que

        
def EN(q,value):
    q.insert(["EN",value])
    return q


for i in x:
    if(i != "D"):
        command,value = i.split()
    else:
        print(q.pop()[1] if not q.empty() else "Empty")
        continue

    dic = {
        "EN" : EN,
        "ES" : ES
    }

    q = dic[command](q,value)