'''def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/400)*100
    return p

marks1=[45,67,88,90,56]
percentage1=percent(marks1)
marks2=[89,97,88,90,86]
percentage2=percent(marks2)
print(percentage1,percentage2)'''

'''average=(sum(marks)/400)*100
x=len(marks)
print(x)'''
def good(name="defaultanonymous"):
    hc=("Goood day "+name)
    return hc
for i in range(2):
    name=input("enter name: ")
    a=good()
    a=good(name)
    print (a)

def mysum(n1,n2):
    return n1+n2
a=int(input("enter n1"))
b=int(input("enter n2"))
s=mysum(a,b)
print(s)