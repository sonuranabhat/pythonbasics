'''
a=int(input("enter marks1: "))
b=int(input("enter marks2: "))
c=int(input("enter marks3: "))
total=(a+b+c)/3
print(total)
if(total>40):
    if((a<33)or(b<33)or(c<33)):
        print("fail")
    else:
        print("pass")
else:
    print("fail")
    '''
text=input("enter the text\n")
if("make a lot of money"in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this"in text):
    spam=True
elif("click this"in text):
    spam=True
else:
    spam=False
if(spam):
    print("the text is spam")
else:
    print("the text is not spam")


'''usr=input("enter username:")
x=len(usr)
print(x)
if(x<10):
    print("less than 10")
elif(x==10):
    print("Equals 10")
else:
    print("more than 10")
'''
names=['hary','sonu','ravi','ram','shyam']
name=input("enter the name yhat you want to search\n")
if name in names:
    print("your name is present in list")
else:
    print("your name is not in the list")
