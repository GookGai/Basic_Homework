def gcd(a,b): 
    if(b==0): 
        return abs(a) 
    else: 
        return gcd(int(b),int(a)%int(b)) 


a= input('Enter Input : ').split(" ")
if(int(a[0])==0 and int(a[1]) == 0):
    print("Error! must be not all zero.")
else:
    if(a[0]>=a[1]):
        max = a[0]
        min = a[1]
    else:
        max = a[1]
        min = a[0]
    s = "The gcd of "+ max+ " and "+min +" is : " 
    print(s,end = '')
    print(gcd(a[0],a[1]))
