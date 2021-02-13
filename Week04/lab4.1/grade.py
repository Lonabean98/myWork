#reads in a students percentage mark and
#prints out corresponding the grade

#Author: Lonan Keane

grade= float(input("Enter the percentage: "))

if grade < 40:
   print("Fail")

elif  40<grade<49:
   print("Pass")

elif  50<grade<59:
    print("Merit 2")

elif  60<grade<69:
    print("Merit 1")

else:
    print("Distinction")
   