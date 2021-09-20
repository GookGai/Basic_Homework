def bub(A):
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]

a = (input("Enter ").split())
lst = [int(i) for i in a]
bub(lst)
print(lst)