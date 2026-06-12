"""DATA TYPES: 
    - String:
        - def: collection of characters
        - enclosed in between either single quotes '' or double quotes ""
        - class: str() => <class 'str'>
        - we can use the str() method to convert from different data types to strings
        - has in-built methods
        - slicing
        - immutable in nature 
    - Numbers:
        - Integers

        - Floating
        - Complex
    - Lists:
        - Set
        - Array
        - Tuple
        - Dictionary

"""
output = '' #global variable 
fruits = ['apple', 'banana', 'grapes', 'orange','apple', 'banana', 'grapes', 'orange'] # list of strings
output = fruits
output =type(fruits)
output = fruits [-1]
output = fruits [3:9]
output = len(fruits)

#TUPLES
COLORS = ["red", "green", "blue", "yellow", "black", "white"]
COLORS = ["red", "green", "blue", "yellow", "black", "white",12,34,56,78,90]#can caputure different data types in a list
output = COLORS
output = type(COLORS)

"""
captures unique elements in a list (no duplcates)
ech element is unordered and unindexed
enclosed in between curly braces {}
class: set() => <class 'set'>

can convert to tuple using the set() method

"""

fruits = ['apple', 'banana', 'grapes', 'orange','apple', 'banana', 'grapes', 'orange'] # list of strings
output = type(fruits)
fruits = {'apple', 'banana', 'grapes', 'orange','apple', 'banana', 'grapes', 'orange'} # list of strings
output = type(fruits)
output = fruits
fruits = ['apple', 'banana', 'grapes', 'orange','apple', 'banana', 'grapes', 'orange'] # list of strings
output = set(fruits)# converts the list to a set and captures only unique elements in the list``


team_one= {"M", "A", "R", "Y"}
team_two = {"M", "A", "R", "Y", "J", "O", "H", "N"}

output = team_one
output = team_two
output = team_one.difference(team_two) #returns elements in team_one that are not in team_two
output = team_two.intersection(team_one)#return scommn elements in both sets
output = team_one.symmetric_difference(team_two)

"""
DICTIONARY:
  -key value pair
  class name dixt
  it is composed of methods
  enclosed in between curly braces {}
after the key we have a colon : and then the value , then a comma to separate the key value pairs
"""
student  ={
    "name": "John Doe",
     "age": 25,
    "index_number": "123456789",
    "course": "Computer Science",   
    
}
output = student
output = type(student)
output = student["course"] #  accessing the value of a key in a dictionary



print ("=============================")
print (output)
print ("=============================")