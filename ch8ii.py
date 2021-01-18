def temp(c):
    f=(c * 9/5) + 32
    return f
def natural(n):
    if(n==0):
        return 0
    return n+natural(n-1)


c=float(input("enter temperature in c: "))
f=temp(c)
print("temp in farenheit is",str(f),end=" ")
print(" DONE NO ENTER",end="\n")
print("NEWLINE")
n=int(input("enter a number"))
s=natural(n)
print(s)
