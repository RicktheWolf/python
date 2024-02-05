
name = ("Pran Krishna")
print(name)
print("This is " + name +" and he is so active")
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())

#asking questions
print(name.isupper())
print(name.islower())
#making them in case and asking
print(name.upper().isupper())
print(name.upper().islower())
print(name.lower().islower())
print(name.lower().isupper())
#asking the legnth of the string or how many characters are in the string
print(len(name))
#index value in the string
print(name[0])
print(name[5])
#checking the value in which index
print(name.index("K"))
#if it is more than one character, this is used to check in which index the character has started
print(name.index("Kri"))
#replacing value with one another
print(name.replace("Pran", "Krishna"))
