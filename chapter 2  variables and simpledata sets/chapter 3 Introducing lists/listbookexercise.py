names = ["ashley", "angela", "names", "angels", "guy"]
count = 0


message = "Hello my name is " 

#both ways but y is lost in enumerate and over shadows
# for x, y in enumerate(names):
#     for x in names:
#         if count < len(names):
#             print(message + x)
#             count += 1
            
#quicker way or
# for name in names:
#     print(message + name)  
    
#same concept but uses count
for x in names:
    if count < len(names):
        print(message + x)
        count += 1