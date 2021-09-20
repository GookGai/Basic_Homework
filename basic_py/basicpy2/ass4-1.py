class Queue:
    
     class Node:

         def __init__(self,value):
             self.value = value
             self.next = None

     def __init__(self):
         self.last = None
         self.first = None
    

     def  insert(self,value):
         newNode = self.Node(value)
         if(self.first == None):
             self.first = newNode
             self.last = newNode
         else : 
             self.last.next = newNode
             self.last = newNode

     def pop(self):
         last = self.first
         value = self.first.value
         self.first = self.first.next
         del last
         return value

     def head(self):
         return self.first.value

     def tail(self):
         return self.last.value

     def empty(self):
         if self.first == None:
             return True  
         else :
             False

     def print(self):
         lst = []
         last = self.first
         while (last != None):
             # print(last.value,end=", ")
             lst.append(last.value)
             last = last.next
         return lst
q = Queue()
dq = Queue()
x = input("Enter Input : ").split(',')

for i in x:
     if(i != "D"):
         command,value = i.split()
     else:
         command = "D"

     if(command == "E"):
         q.insert(value)
         print(*q.print(),sep=", ")
     elif(command == "D"):
         if(q.empty()):
             print("Empty")
         else:
             pop = q.pop()
             dq.insert(pop)
             print(pop,"<- ",end="")
             print(*q.print() if not q.empty() else "Empty",sep=", " if not q.empty() else "")
        
print(*dq.print()if not dq.empty() else "Empty",sep=", " if not dq.empty() else "",end="")
print(" : ",end="")
print(*q.print() if not q.empty() else "Empty",sep=", " if not q.empty() else "")
