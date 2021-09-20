a = input('Enter Input : ').split(',')
ls = list()
for i in a:
    w,f = i.split()

    if len(ls) == 0:
         ls.append(i)
    else:
        back = ls[-1:][0]
        nw,nf = back.split()
        while int(w) > int(nw):
            print(nf)
            ls.pop()
            if len(ls) > 0:
                back = ls[-1:][0]
                nw,nf = back.split()
            else:
                break
        ls.append(i)