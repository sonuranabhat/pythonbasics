n=int(input("enter the number "))
for i in range (11):
    #print(str(n)+"*"+str(i)+"="+str(n*i))
    #not workprint(n+"*",i,"=",n*i)
    print(f"{n}X{i}={n*i}")
sum=0
fact=1
for i in range(1,n+1):
    sum=sum+i
    fact=fact*i
print (sum)
print(f"the factorial of {n} is {fact}")
prime=True
for i in range (2,n):
    if (n%i==0 and n!=2) :
        prime=False
        break
if prime:
    print("prime")
else:
    print("not prime")

l1=["harry","soham","sachin","sonu","rahul"]
for name in l1:
    if  name.startswith("s"):
        print("Hello"+name)
for name in l1:
    if  name[0]=="s":
        print("Hello"+name)