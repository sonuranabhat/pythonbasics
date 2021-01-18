def pattern(n):
    for i in range (n):
        print("*"*(n-i))
n=int(input("enter no of rows"))
p=pattern(n)
def inches(a):
    return a/2.54
a=int(input("enter in centimeter"))
print(inches(a))
def mul(n):
    for i in range (1,11):
        print (f"{n}X{i}={n*i}")
n1=int(input("enter a number"))
mul(n1)
