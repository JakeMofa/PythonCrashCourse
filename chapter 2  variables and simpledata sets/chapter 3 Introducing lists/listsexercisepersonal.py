bicycles = ['trek', 'cannondale', 'redline', 'specialized']
word = "redline"
count = 0
res = []

#checks if y in word and  appends and gives us it back
# for x, y in enumerate(bicycles):
#     if y in word:
#         res.append(y)
#         print(res)
        
        
        
#checks if x in word, appends to word, and increments index + 1 and prints that out
for x, y in enumerate(bicycles):
    if y in word:
        res.append(y)
        
        if x + 1 < len(bicycles):
            res.append(bicycles[x+ 1])
        
print(res)

#this is manual indexes and vlaues
#for x in  range(len(bicycles)):
    #print(x, bicycles[x])
    
    
# this gives you only the indexs
#for x in range(len(bicylcles)):
    #print(x)

#this gives you both , index and value
#for x, y in enumerate(bicycles):
    #print (x, y)
    

#loops through and gives you all keys
#for x in  bicycles:
    #print(bicycles)
    


#for i in len(bicycles):
    #print(i)
    
    
    
## uses to check if len of bicles is 0 if not say its empty list if it is not goes to else and runs other functions
#if len(bicycles) == 0:
#    print("no inventory")
#else:
#    for x, y in  enumerate(bicycles):
#        print(x, y)



  
