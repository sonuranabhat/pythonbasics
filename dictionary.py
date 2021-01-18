'''
dict={
    "fast":"quicklwy",
    "fast":"quicks",
"sonu":"coder",
"hungry":"fast",
"fast":"quickly",#in muliple keys it prints last key of fast ie quickly
"marks":[1,2,3],
"anotherdict":{'sound':'music',
'dance':'movement',
'act':'drama'}}
dict['marks']=[45,45,90]
print(dict)
print(dict['fast'])
print(dict['marks'])
print(dict["anotherdict"])
print(dict["anotherdict"]['sound'])
'''
dict={
    "one":1,
    2:4,3:6,4:8,
"sonu":"coder",
"hungry":"fast",
"fast":"quickly",
"marks":[1,2,3],
"anotherdict":{'sound':'music',
'dance':'movement',
'act':'drama',
'sonu':'player'}
}
print(type(list(dict)))#convert to list
print(dict.keys())#prints keys
print(dict.values())#prints values
print(dict.items())#shows in(key,value)format
print(dict)
uplist={"sonu":"dancer",
1:2,222:333}
dict.update(uplist)
print(dict)
print(dict.get("fast"))#doesnt throw error shows none
print(dict["fast"])


 