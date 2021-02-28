
def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice


def doAdd(students):
  currentStudent = {}
  currentStudent["name"]=input("enter name :")
  currentStudent["modules"]= readModules()
  students.append(currentStudent)
 

def readModules():
 modules=[]
 moduleChoice=input("enter first module name (blank to quit):")

 while moduleChoice != "":
  module= {}
  module["name"]=moduleChoice
  module["grade"]= input("enter grade:")
  modules.append(module)
  moduleChoice= input("enter next module name (blank to quit)")
  
  return modules

 
def displayModules(modules):
 print ("\tName \tGrade")
 for module in modules:
    print("\t{} \t{}".format(module["name"], module["grade"])) 

def doView(students):
  for currentStudent in students:
    print(currentStudent["name"])
    displayModules(currentStudent["modules"])

students = []
choice = displayMenu()
while (choice != "q"):
    if choice == "a":
        doAdd(students)
    elif choice== "v":
        doView(students)
    elif choice != "q":
        print("Please choose a, v or q")
    choice=displayMenu() 

    