str = input('Enter String : ')
last = -1 
temp = []
ans = []
list = []
for x in str:
    list.append(x)

for y in list :
    if(y in temp): 
        ans.append(temp.index(y))
    else:   
        temp.append(y)
        last+=1
        ans.append(last)
print(ans)


