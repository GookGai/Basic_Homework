a = input('Enter Input : ').split()
ls = list()
countls = list()
combo = 0
for i in a:
    if len(ls) == 0:
        ls.append(i)
        countls.append(1)
    elif ls[-1] == i:
        if countls[-1] + 1 == 3:
            combo += 1
            for j in range(2):
                ls.pop()
                countls.pop()
        else:
            ls.append(i)
            countls.append(2)
    else:
        ls.append(i)
        countls.append(1)
ls.reverse()
print(len(ls))
for j in range(len(ls)):
    print(ls[j],end = '')
if len(ls) > 0:
    if combo > 1:
        print("\nCombo :", combo, "! ! !")
else:
    print("Empty")
    if combo > 1:
        print("Combo :", combo, "! ! !")

    