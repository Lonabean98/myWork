
#input string to be changed
#Author: Lonan Keane 


string = input(str(" please enter a string:"))

output = string.strip().lower()

lenghtin = len(string)
lenghtout = len(output)

print( " That string normalised is :{}".format(output))
print( "we reduced the input string from {} to {} characters".format (
    lenghtin, lenghtout))






