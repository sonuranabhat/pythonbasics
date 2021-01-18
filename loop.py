i=1
while(i<=50):
    print(i,"Yes")
    i=i+1
list=["sonu","si","a","girl","coder"]
i=0
while(i<len(list)):
    print(list[i])
    i=i+1
for item in list:
    print(item)
l=[1,7,8]
#for else loop same as while else loop
for item in l:
    print(item)
else:
    print("Done")
#pass=null statement in python and it instruct to do nothing
l=[1,4,5,6,6,7]
for i in l:
    pass
for i in range(2,9):
    if i==5:
        continue
    print (i)
#stepsize
for i in range(10,40,2):
    print (i)
#break
    if i==20:
        break
else:
    print("this is inside else for")
