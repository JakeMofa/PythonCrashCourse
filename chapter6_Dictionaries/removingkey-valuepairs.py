alien_0 = {'color' :'green', 'point' : 5, 'numbers' : 4, 'name':'issac'}

del alien_0['point']

print(alien_0)

word  = 'green'

for key , value in alien_0.items():
    if word == value:
        print(f'{key}')