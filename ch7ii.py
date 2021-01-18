n=int(input("enter no of rows "))
for i in range (n):
    print("*"*(i+1))
for i in range (n):
    print("p"*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print("q"*(n-i-1))


for i in range(0,n):
    if i==0 or i==n-1:
        print("*" * (n),end="")
    else:
        for j in range(0,n):
            if j==0 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
    print()

for i in range(10,0,-1):
    print(f"{i}X{n}={i*n}")
    