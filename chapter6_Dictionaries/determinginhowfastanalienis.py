alien_0 = {'x_postion' : 0, 'y_position': 25, 'speed' : 'medium'}  #so if we want to change the speed, fast, medium , slow
print(f'Original position of this is {alien_0["x_postion"]}')

#determine how fast and slow this alien is?
if alien_0['speed'] == 'slow':
    x_incrementalspeed = 1
elif alien_0['speed'] == 'medium':
    x_incrementalspeed = 2
else:
    x_incrementalspeed  = 3
    

alien_0['x_postion'] =  alien_0['x_postion'] + x_incrementalspeed
print(f' this is the current speed of x position {alien_0["x_postion"]}')