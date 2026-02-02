#usig  the range function
for value in range(1,5):
    print(value)
    
    
#using range functinos to create a list
numbers = list(range(1,20))
print(numbers)


#this allows me to use the even numbers and set it by the first being how to start, middle total and the end by how many times it shoudl be
evennumbers = list(range(2,20,2))
print(evennumbers)

# we can even get the square  numbers  of each interger within the range
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    
print(squares)


## we can write this code shorter
box = []

for number in range(1,5):
    box.append(number**2)
    
print(box)



## simple statistics with a list of number
digits = [0,1, 2, 3, 4,5, 6, 7, 8, 9 , 10]

print(max(digits))
print(min(digits))
print(sum(digits))


#list Comprehensions we can shorten all of this if we need too
mul = [iron **2 for iron in range(1,10)]
print(mul)

