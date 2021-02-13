
#Author: Lonan Keane

import random


answer = random.randint(0,100)
guess= int(input("please guess the number: "))

while guess!= answer:
   if guess > answer:
    print("Too high")
   elif guess < answer:
       print("Too Low")

   guess=int(input("Please guess again: "))

print("Well done! Yes the number was {}" .format(guess))



