#program that  reads in two numbers and divides the first one
#by the second and give the integer result and the remainder.

#inputs for first number and number you want to divide by
x = int(input("enter first number:"))   
y = int(input("enter number you want to divide by:"))  

z = int(x//y)    #z is numbers divided as an integer
remainder = x%y  #remainder using modulus

#print result
print("{} divided by {} is {} with remainder of {}" .format (x,y,z,remainder))