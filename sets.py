a={1,2,3,4,2,2,3,5}#ignores repitition
print(type(a))
print (a)
#empty dictionary a={}
#empty set
s=set()
print(type(s))
s.add(4)
s.add(5)
s.add(6)
s.add(7)
s.add(8)
s.add(9)
s.add((6,7,8))
print(s)
print("length",len(s))
s.remove(4)
print(s)
print(s.pop())

print (s)