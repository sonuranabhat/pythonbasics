def strp(this,word):
    newstring=this.replace(word,"")
    return (newstring.strip())


#this="                  Sonu is good       "
this=input("enter the unstripped sentence: ")
word=input("enter the word you want to remove: ")
n=strp(this,word)
print (n)
