class Queue:
    def __init__(self, li=None):
        if li == None:
            self.queue = []
        else:
            self.queue = li

    def enQueue(self, i):
        self.queue.append(i)

    def deQueue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def clear(self):
        return self.queue.clear()

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def getIndex(self, i):
        return self.queue.index(i)

    def getCopy(self):
        return self.queue.copy()


inp = input("Enter Input (Normal, Mirror) : ").split()

temp_normal = Queue()
temp_mirror = Queue()
normal = Queue()
mirror = Queue()
defuser = Queue()

failed_interrupted_count = mirror_count = normal_count = 0


for i in list(reversed(inp[1])):
    
    if temp_mirror.size() == 0 or temp_mirror.peek() == i:
        temp_mirror.enQueue(i)
        if temp_mirror.size() == 3:
            
            defuser.enQueue(i)
            temp_mirror.clear()
            mirror_count += 1
    else:
       
        while temp_mirror.size() != 0:
            mirror.enQueue(temp_mirror.deQueue())
            
            if mirror.size() >= 3 and (mirror.getCopy()[-3] == mirror.getCopy()[-2] == mirror.getCopy()[-1]):
                defuser.enQueue(mirror.getCopy()[-1])
                mirror = Queue(mirror.getCopy()[:-3])
                mirror_count += 1
        
        temp_mirror.enQueue(i)
else:
    while temp_mirror.size() != 0:
        mirror.enQueue(temp_mirror.deQueue())
        if mirror.size() >= 3 and (mirror.getCopy()[-3] == mirror.getCopy()[-2] == mirror.getCopy()[-1]):
            defuser.enQueue(mirror.getCopy()[-1])
            mirror = Queue(mirror.getCopy()[:-3])
            mirror_count += 1
           
    mirror = Queue(list(reversed(mirror.getCopy())))
    
for i in inp[0]:
  
    if temp_normal.size() == 0 or temp_normal.peek() == i:
        if temp_normal.size() == 2 and defuser.size() != 0:
            x = defuser.deQueue()
           
            if temp_normal.peek() == x:
               
                temp_normal.clear()
                normal.enQueue(i)
                failed_interrupted_count += 1
            else:
               
                while temp_normal.size() != 0:
                    normal.enQueue(temp_normal.deQueue())
                  
                    if normal.size() >= 3 and (normal.getCopy()[-3] == normal.getCopy()[-2] == normal.getCopy()[-1]):
                        normal = Queue(normal.getCopy()[:-3])
                        normal_count += 1
                      
                normal.enQueue(x)
                temp_normal.enQueue(i)
        else:
            temp_normal.enQueue(i)
            if temp_normal.size() == 3:
              
                temp_normal.clear()
                normal_count += 1
    else:
       
        while temp_normal.size() != 0:
            normal.enQueue(temp_normal.deQueue())
           
            if normal.size() >= 3 and (normal.getCopy()[-3] == normal.getCopy()[-2] == normal.getCopy()[-1]):
                normal = Queue(normal.getCopy()[:-3])
                normal_count += 1
               
        temp_normal.enQueue(i)
else:
    while temp_normal.size() != 0:
        normal.enQueue(temp_normal.deQueue())
        if normal.size() >= 3 and (normal.getCopy()[-3] == normal.getCopy()[-2] == normal.getCopy()[-1]):
            normal = Queue(normal.getCopy()[:-3])
            normal_count += 1
           
    normal = Queue(list(reversed(normal.getCopy())))

print('NORMAL :')
print(normal.size())
if normal.size() != 0:
    print(''.join(normal.getCopy()))
else:
    print('Empty')
print(f'{normal_count} Explosive(s) ! ! ! (NORMAL)')
if failed_interrupted_count != 0:
    print(f'Failed Interrupted {failed_interrupted_count} Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(mirror.size())
if mirror.size() != 0:
    print(''.join(mirror.getCopy()))
else:
    print('ytpmE')
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirror_count}')