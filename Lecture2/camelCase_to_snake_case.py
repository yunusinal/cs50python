"""
implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user's input will indeed be in camel case.
"""
inp=input("kelime:")
for i in inp:
    if i.isupper():
        x,y = inp.split(i,1) #if there is upper character split from there
        x=x+"_" #add _ end of first part
        i=i.lower()  # lower the Upper character and add the character becuse we lost the charachter when splitting.
        y=i+y
        inp=x+y # merge this 2 list and do the procces again.

print(inp)
      
    





