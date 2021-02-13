# keeps reading numbers until the user
#enters a 0. 

group= [int((input("enter number (0 to quit): ")))]
avg= sum(group)/len(group)

while group!= 0:
    group.append(group)

for x in group:
    print(x)
    print("The average is {}" .format(avg))
    if x == 0:
        break
     
