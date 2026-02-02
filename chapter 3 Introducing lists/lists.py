bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#accessing lists

print(bicycles[0])

#print(bicycles[0].title())

print(bicycles[1])
print(bicycles[2])
#prints the last value within a  list
print(bicycles[-1])

#now concatenating messages with lists

message = " Hello my name is " + bicycles[0].title() + " and i am " + bicycles[-1]

print(message)