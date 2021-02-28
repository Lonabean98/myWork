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


 