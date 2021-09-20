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

        
me = Queue()
meP = Queue()
you = Queue()
youP = Queue()

act = {
    0 : "Eat",
    1 : "Game",
    2 : "Learn",
    3 : "Movie"
}
place = {
    0 : "Res.",
    1 : "ClassR.",
    2 : "SuperM.",
    3 : "Home"
}

x = input("Enter Input : ").split(',')
score = 0
for i in x:
    m,y = i.split()
    me.insert(m)
    you.insert(y)
    
    mA,mP = m.split(':')
    yA,yP = y.split(':')
    meP.insert(act[int(mA)]+":"+place[int(mP)])
    youP.insert(act[int(yA)]+":"+place[int(yP)])
  

    logic = [1 if mA == yA else 0 ,2 if mP == yP else 0]
    
    sc = 1 << sum(logic)
    sc = sc >> 1
    
    score += sc if sc != 0 else -5 

print("My   Queue = ",end="")
print(*me.print(),sep=", ")
print("Your Queue = ",end="")
print(*you.print(),sep=", ")
print("My   Activity:Location = ",end="")
print(*meP.print(),sep=", ")
print("Your Activity:Location = ",end="")
print(*youP.print(),sep=", ")

if(score > 6):
    print("Yes! You're my love! : Score is ",end="")
elif(score >= 0):
    print("Umm.. It's complicated relationship! : Score is ",end="")
else:
    print("No! We're just friends. : Score is ",end="")
print(score,".",sep="")