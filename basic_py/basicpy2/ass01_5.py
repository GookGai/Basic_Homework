a = int(input('Enter Input : '))
sizes = 2*a+4
count = 0
t =0
z=0
for i in range(sizes):
    if(count == 0 ):
        for j in range(sizes):
            if(j<a+1): print('.',end = '')
            elif(j == a+1): print('#',end = '')
            elif(j == a+2): print('+',end = '')
            else :print('+', end = '')
    elif(count<a+1):
        for j in range(sizes):
            if(j<a+1):
                if(j<a-t): print('.',end = '')
                else:print('#',end = '')
            elif(j == a+1): print('#',end = '')
            elif(j == a+2): print('+',end = '')
            elif(j<sizes-1): print('#',end = '')
            else:print('+',end = '')
        t+=1
    elif(count<a+3):
        for j in range(sizes):
            if(j<a+2): print('#',end = '')
            else:print('+',end = '')
    elif(count<sizes-1):
        print('#',end ='')
        for j in range(sizes-1):
            if(j<a):print('+', end ='')
            elif(j == a): print('#',end = '')
            elif(j == a+1): print('+',end = '')
            else:
                if(j<sizes-2-z): 
                    print('+',end = '')
                else:print('.',end ='')
        z+=1
    else:
        for j in range(sizes):
            if(j<a+2): print('#',end = '')
            elif(j == a+2): print('+',end = '')
            else :print('.', end = '')
    count += 1
    print('')