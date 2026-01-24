motorcycles = ['1 honda', 'yamaha', 'suzuki']
print(motorcycles)

#ways of directly addding elements directly to the list
motorcycles[0] = '  2tomaha'

print(motorcycles)

#appending another element to the list
motorcycles.append('3ducati')
print(motorcycles)


#we can append  new elemenrs to an empty list
bikes = []
bikes.append('3 tomahawk')
bikes.append('bmw')
bikes.append('honda')
bikes.append('to test')
print(bikes)

# we can insert new elements in a list any any postions

bikes.insert(0, ' 4 first bike')

print(bikes)


#now if we want to remove elements
del bikes[1]
print(bikes)


bikenames = [' 5honda ' , ' yahama ', ' suzuki ' ]
print(bikenames)

bikenamep =  bikenames.pop()
print(bikenamep)
#add the pop messaged sentence:

print('my last bike i had was a ' + bikenamep)


# we can remove a motorcycle from a  list using the pop methods

# we can also remove an item from a list by using  its value
testnames = [' 5honda ' , ' yahama ', ' suzuki ' ]

testnames.remove(' yahama ')
tryname = ' suzuki '

testnames.remove(tryname)

print(testnames)

print(" my name is jake and the bike" + tryname + "is too expensive for me") 


