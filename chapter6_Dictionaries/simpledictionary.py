alien_0 = {'color' :  'green ' , 'point' : 5}

# print(alien_0['color'])
# print(alien_0['point'])
words =  'green'

new_points =  alien_0['point']

print(f'you have earned {new_points} new points ')


for key, value in alien_0.items(): #we have to turn value into a string becasue it assumes the word value is not a string
    if words in str(value):
        print(f'this is the value {key}')


    