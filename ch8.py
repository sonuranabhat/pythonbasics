def great(a,b,c):
    if(a>b and a>c):
        g=a
    elif(b>a and b>c):
        g=b
    else:
        g=c
    return g    
a=int(input("enter n1: "))
b=int(input("enter n2: "))
c=int(input("enter n3: "))
max=great(a,b,c)
print("greatest num is: ",str(max))
