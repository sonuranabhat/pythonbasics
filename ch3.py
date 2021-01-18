n=input("enter a name:\n ")
greet="Good afternoon,"
print(greet+" "+n)
letter='''dear <|name|>, 
you are selected!<|date|>
have a great day
thanks and regrards
bill
<|date|>'''
name=input("name \n")
date=input("date\n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print (letter)
s="skjd dnc jdn djn jd....j"
#s=s.replace("..",".")
print(s.replace("..","."))
#print (s)

