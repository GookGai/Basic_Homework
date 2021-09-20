
def print1ToN(n):
    if n<1 :
        return 1
    else:
        print1ToN(n-1)
        print(n,end =" ")


def printNto1(n):
    if n<1 :
        print(1,end =" ")
        return 1
    elif n == 1:
        print(1, end = " ")
    else:
        print(n,end =" ")
        return printNto1(n-1)

n = int(input("Enter Input : "))
print1ToN(n)
printNto1(n)