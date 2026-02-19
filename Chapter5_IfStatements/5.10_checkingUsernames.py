current_users = ['jake', 'james', 'cole', 'animal', 'geek']
new_users = ['jake', 'james' , 'kesiha' , 'diego', 'anchez']



curren_lower_user = [user.lower() for user in new_users]

for user in current_users:
    if user.lower() in new_users:
        print(f'this user {user} is already there')
    else:
        print(f' add {user} to the new username ')
    




#this was y
# current_users = ['jake', 'james', 'cole', 'animal', 'geek']
# new_users = ['jake', 'james' , 'kesiha' , 'diego', 'anchez']



# for  user in new_users:
#     if user in current_users:
#         print(f'this user is already taken {user}')
#     else:
#         print(f'we can use this username {user}')