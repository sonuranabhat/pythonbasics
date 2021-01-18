def pattern(n):
    for i in range (n):
        print("*"*(n-i))
n=int(input("enter no of rows"))
p=pattern(n)
print(p)