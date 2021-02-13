#generates 10 random numbers (0-100) ,
#prints them out then prints out the top three.

#Author: Lonan Keane
import random
#create empty list
numbers = []

for i in range(0,10):
    number = random.randint(0,100)
    numbers.append(number)
    

print("10 random numbers {} ".format(numbers))
print("The top 3 are {}".format(max(numbers)))