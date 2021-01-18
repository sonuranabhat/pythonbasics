def simp(a):#parameter/formal parameter
    p=1
    for i in range(a):
        p=p*(i+1)
    return p
def recursive(a):#parameter/formal parameter
    if a==1 or a==0:
        return 1
    return a*recursive(a-1)

x=int(input("enter any number: "))
fact1=simp(x)#argument and actual paramter
fact2=recursive(x)#argument and actual parameter
print(fact1)
print(fact2)