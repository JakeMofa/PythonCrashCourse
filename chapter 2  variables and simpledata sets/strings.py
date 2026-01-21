name = "ada title low"
print(name.title())


#but we also  have functions that do the upper and lower

print(name.upper())
print(name.lower())


## concatenattion of words

first_name = "ada"
last_name = "luis"
full_name = first_name + " " + last_name

print(full_name.title())

## this adds a space, tab within a string
print("\t python")


## this adds a new line  within a string
print("\n python \t demons , \n words")



##stripping white spaces from within strings

favwords = ' lookslike w '
favwords =  favwords.rstrip()
favwords = favwords.lstrip()

print(favwords)
