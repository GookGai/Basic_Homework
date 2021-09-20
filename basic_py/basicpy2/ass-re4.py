# perket
def findLength(num,div):
    
    if( 1 << div >= num):
        return  div
    else:
        return findLength(num,div+1)

def getDecimal(num,res):
    
    if(num==0):
        return res
    res = str( (num) & 1) + res

    return getDecimal(num >> 1,res)


lst = []
def decimal(num,l,max,ans = None):
    
    if(num > max):
        return ans
    dec = getDecimal(num,"")
    tryAll =  ((l - len(dec)) * "0") +dec 
    s = 1
    b = 0
    for i in range(0,len(tryAll)):
        if(tryAll[i] == "1"):
           s *= int(lst[i].split()[0])
           b += int(lst[i].split()[1])

    if(ans == None):
        ans = abs(s-b)
    else:
        ans = ans if abs(s-b) > ans else abs(s-b)

    return decimal(num+1,l,max,ans)

lst = input("Enter Input : ").split(',')
x = len(lst)
l = findLength(2**x-1,1)
l = int(l)
ans = decimal(1,l,2**x-1,None)
print(ans)