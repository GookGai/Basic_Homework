a = input('Enter String : ')
p = []
k = []
count = 0
for s in range(len(a)):
        if(a[s] != a[s]):
            k.append(a[s])
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i] == a[j]):
            p.append(j)
            break

print(k)
print(p)