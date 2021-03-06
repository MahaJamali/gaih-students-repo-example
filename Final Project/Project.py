# -*- coding: utf-8 -*-
"""Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Is4vkYKVlTP5j3pH7c3KgOXdFS0HNSU3

Compay Management System

Employee class with attributes of name, age and language. It has 6 methods and below are there details :
1 - Print employee name
2 - Display age of employee
3 - Add new language
4 - Remove language
5 - Show employee information
6 - Show employee language that he can speak
"""

class Employees:

    def __init__(self, name, age):
        self.name     = name
        self.age      = age
        self.language = set()
        self.manager  = {}
    
    def printEmployeeName(self):
        print("Name :",self.name)
    
    def displayAge(self):
        print("Age", self.age)
        
    def addNewLanguage(self,new_lang):
        self.language.add(new_lang)

    def removeLanguage(self, lang):
        self.language.remove(lang)

    def showEmployeeInfo(self):
        print("{} is {} years old and he can speak {}".format(self.name,self.age, self.language))

    def displayEmpllang(self):
      print ("He can speak following language :")
      for lang in self.language:
        print(lang)

"""Manager class and it is inherited from parent class of Employees"""

class Manager(Employees):
  pass

  def __init__(self, name,age):
      super().__init__(name, age)

"""Program to get the languages that any of the employee can speak by using function, *args and set."""

employeeLanguage = set()

def getLanguageEmployeesSpeak(*args):
  global employeeLanguage
  for employee in args:
    for lang in employee.language:
      employeeLanguage.add(lang)
      
  return employeeLanguage

"""Add new manager and employees and display there name, age and languages. In the end print the langauges that any employee can speak. """

Louis = Manager("Louis",43)
Louis.addNewLanguage("English")
Louis.addNewLanguage("Turkish")

Lunna = Employees("Lunna",23)
Lunna.addNewLanguage("English")
Lunna.addNewLanguage("Chinese")

David = Employees("David",23)
David.addNewLanguage("English")
David.addNewLanguage("Spanish")

print("Printing Manager Information")
Louis.printEmployeeName()
Louis.displayAge()
Louis.displayEmpllang()

print("Printing Employees 1 Information")
Lunna.printEmployeeName()
Lunna.displayAge()
Lunna.displayEmpllang()

print("Printing Employees 2 Information")
David.printEmployeeName()
David.displayAge()
David.displayEmpllang()

print("Printing the languages that any employee can speak")
languages = getLanguageEmployeesSpeak(David,Louis,Lunna)
print(languages)