class Queue:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def enQueue(self, i):
        self.items.append(i)  # insert i ที่ท้าย list

    def deQueue(self):
        self.items.pop(0)  # pop out index 0
        # print(self.items[0])

    def isEmpty(self):
        return self.items == []  # return len(self.items) == 0

    def size(self):
        return len(self.items)

####################################################################

# Function
# เพิ่มค่าตามเลข ascii
def encodemsg(q1, q2):
    temp = 0
    length = len(q1.items)
    s = ''
    for i in range(len(q1.items)):
        temp = ord(q1.items[i])
        if temp < 123 and temp > 96:
            temp += q2.items[i]
            if temp >= 123:
                temp -= 26
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
            else:
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
        elif temp < 91 and temp > 64:
            temp += q2.items[i]
            if temp >= 91:
                temp -= 26
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
            else:
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
    for d in range(length):
        q1.deQueue()
    print('Encode message is : ', q1.items)

# ลดค่าตามเลข ascii
def decodemsg(q1, q2):
    temp = 0
    length = len(q1.items)
    s = ''
    for i in range(len(q1.items)):
        temp = ord(q1.items[i])
        if temp < 123 and temp > 96:
            temp -= q2.items[i]
            if temp <= 96:
                temp += 26
                s = chr(temp)
                q1.enQueue(s)
            else:
                s = chr(temp)
                q1.enQueue(s)
        elif temp < 91 and temp > 64:
            temp -= q2.items[i]
            if temp <= 64:
                temp += 26
                s = chr(temp)
                q1.enQueue(s)
            else:
                s = chr(temp)
                q1.enQueue(s)
    for d in range(length):
        q1.deQueue()
    print('Decode message is : ', q1.items)

####################################################################

# Main
m, n = input('Enter String and Code : ').split(',')
string = []
number = []
for i in m:
    if i != ' ':
        string.append(i)
for j in n:
    number.append(int(j))

q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)