a=["hello",2,3.7,False,56,7]
a[1]=98
print (a)
print(type(a))
#list slicing
x=["z","x","y","a",45,4,0]
print(x[-4:])
print(x[1:7:2])
print(x[::])
v=[1,4,3,6,8,2,5]
print(v)
v.reverse()
print(v)
v.append(23)
print(v)
v.sort()
print(v)
v.insert(6,700)#(index,value)
v.pop(2)#index
v.remove(8)#value
print(v)
v.count(1)
print(v)