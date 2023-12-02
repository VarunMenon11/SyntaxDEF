# ==========================================================================================================
# Basic Syntax
# ==========================================================================================================

# ==========================================================================================================
# Variable -> Variables are reserved memory location. It is used to store data for late use. It can
#           contain numbers, decimals, symbols, characters. 
# ==========================================================================================================

a = 10
b = 'Hello'
c = 10.5
d = [2,4,5,6,7]
e = {'m':5, 'n':6}
print("\n\n")

# ==========================================================================================================
# Data Types -> serveral Data types Like Integer (a whole number), Float (whole and Decimal number),
#              String (An array/sequance of characters), Boolean (represents either True or False),
#               List([], values placed in the enclosed square brackets), Dictionary (key-value pairs, 
#               enclosed in curly braces ({}))
# ==========================================================================================================

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print("\n\n")

# ==========================================================================================================
# Comments -> Comments are used to add explanatory notes in your code and are ignored by the 
#             Python interpreter. Single-line comments start with a hash symbol (#) Multi-line comments 
#              can be enclosed in triple quotes (''' ''') or triple double quotes (""" """):
# ==========================================================================================================

#hello

''' 
Hello
kdajdad
dkadad
'''

# ==========================================================================================================
# Print Statement -> The print() function is used to display output on the console.
# ==========================================================================================================

print(a)
print(b)
print(c)
print("\n\n")

# ==========================================================================================================
# Decision Making -> Decision Making is the expectation of the condition given in the program and
#                   specifies which action should be taken according to the condition. 
#                   non-zero and non-null are taken as TRUE and zero and null are taken as FALSE.
# ==========================================================================================================

if a:
    print(a, " is integer")
elif False:
    print(b, " is a str")
else:
    print("Else Statement")
print("\n\n")


# ==========================================================================================================
# Loops -> Loops are used to execute the same line repeatedly as long as the condition is true. 
#          This prevents writing of same line with different value entered multiple times.
#          Types : (a)for loop: iterates over a sequence (e.g., a list, string, or range).
#                  (b)while loop: executes a block of code repeatedly as long as a condition is true.
# ==========================================================================================================

i = 0
for i in range(0, 10):
    print(i)
print(' ')
while i >= 0:
    print(i)
    i = i - 1

print("\n\n")

# ==========================================================================================================
# Function -> Functions are a block of reuseable code, that is used to perform a single, related action
#             Function created by the user is User-defined Function. Any input parathesis or arguments 
#             should be place in curve brackets (()). It should be first define in the function.
# ==========================================================================================================

def add(n1, n2):
    sum = n1 + n2
    print(sum)

add(a, c)
print("\n\n")

# ==========================================================================================================
# Inputs -> Input() function help in reading data from the keyboard(user) from the console. it returns
#           users input as string. Input() function is written inside a datetype box to ask for 
#           Specific data type input only.
# ==========================================================================================================

str = input("Enter a sentence:- ")
print("Str is a ", type(str))

num = int(input("Enter a integer number:- "))
print("num is a ", type(num))

num = float(input("Enter a integer number:- "))
print("num is a ", type(num))
print("\n\n")

n = int(input("Hello"))
a = list(int(num) for num in input().strip().split())[:n] #This is used to place a a string of number in space into a list without using loops

# ==========================================================================================================
# Module -> A module is a file consisting of python codes(AKA Libraries). it is imported into 
#           python by using 'import' statement. 
#           ways to import :- (a) import module : imports the whole module into the code
#                             (b) from modname import module : imports a specific function from the library
#                             (c) from modcase import specfic as soemthng : imports a specific function
#                                 from the library and provide something as a nickname to it.
#                             (d) from . import specfic : imports the specific function after looking 
#                                  through every library folder for it. 
#           
#           To import another ur python file into another python file, we can use import statment. 
#           When using a function from a module, use the syntax: module_name.function_name. 
# 
#           The Dir() function prints out all the function names in a module. Use this to understand the 
#           module more, also ur python files that u have imported
# ==========================================================================================================

import math
print(math.sqrt(4))

from math import sqrt
print(sqrt(4))

from math import sqrt as sqr
print(sqr(4))
print("\n\n")

# ==========================================================================================================
# Exception Handling -> An event, which occurs during the run time and disrupt it. It is a program 
#                       way of saying it has encountered a situation that it cant cope up with.
#                       [do search more info about the different types of exception]
# ==========================================================================================================


try: # program will try these codes
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError: #if the exception(i.e IOerror) is raised, it will execute this block or else wont
   print ("Error: can\'t find file or read data")
except ImportError: # if this exception(i.e ImportError) is raised, it will execute this block or else wont
    print("ImportError ")
else: # if no exception, this block will execute.
   print ("Written content in the file successfully")
   fh.close()
finally:
    print("Helloooooooo") #whether exception is raised or not, this will always be executed

def functionName( level ):
   if level <1:
      raise Exception(level) #use raise to raise an exception
      # The code below to this would not be executed
      # if we raise the exception
   return level

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e: #by Raising, we have raised this exception, hence its blocks would be executed
   print ("error in level argument",e.args[0])



# ==========================================================================================================
# FIle I/O -> Python provides basic functions and methods necessary to manipulate files by default. 
#             You can do most of the file manipulation using a file object.
#             File Handling -> (a) "r" -> Read. If not existing, it return error(IOError)
#                              (b) "w" -> write. If not existing, it creates
#                              (c) "a" -> Appends the file, if not existing, it creates
#                              (d) "b" -> Binary Mode
#             You can use multiple Handling together.... eg) f = open("Text.txt", "rb") to read in binary mode
#             [Do search about different types of mode u can open a file]
# ==========================================================================================================

fo = open("testfile.txt", "w") #this syntax is used to open a file, first argument consist of the file name and the second argument shows the mode u have opened the file

print ("Name of the file: ", fo.name) #this function returns the name of the file

print ("Closed or not : ", fo.closed)# this function returns true or false whether the file is closed or not

print ("Opening mode : ", fo.mode)# this function returns the 2nd agurment

fo.write( "Python is a great language.\nYeah its great!!\n") #to write something into the file, we use this function

fo = open("testfile.txt", "r") # 'w' mode is used to write into the file and 'r' mode is used to read something out of the file

str = fo.read(10) # To read something out of the file, we use this function, argunment is taken to read only that much index of the file
print ("Read String is : ", str)

str = fo.readline() # To read only one line
print ("Read String is : ", str)

position = fo.tell() #Returns the position of the file located
print ("Current file position : ", position)

position = fo.seek(0, 0)# Reposition pointer at the beginning once again

fo.close() # this function closes the file opened.


# ==========================================================================================================
# Scope -> A variable is only available from inside the region it is created.
#          2 Types -> (a) Local scope: A variable created inside a function can only be used by inside the
#                         function. If there is a function inside the function, then variable inside a 
#                         function is available to the nested function too
#                         The "global keyword" converts the loval variable into global variable.
#                     (b) Global Scope: A variable created outside the function is global and can be used 
#                         by anyone. If u operate with same variable inside and outside of a function, then
#                         the print() func inside the function will use the local variable inside the func 
#                         and the print() function outside the function will use the global variable
# ==========================================================================================================

t = 200 # Global Variable
y = 100

def Scope():
    global y
    y = 150 # A local variable converted to a global variable
    t = 250 # A Local Variable
    def Scopein(): # A nested function inside a function
        print("Local t :- ",t)
        print("Local y:- ", y)
    Scopein()

print("Global :- ", t)
print("Global :- ", y)

# ==========================================================================================================
# Python Datetime -> Import datetime to work with date objects
#                    if u want to learn more go to:- https://www.w3schools.com/python/python_datetime.asp
# ==========================================================================================================

import datetime

x = datetime.datetime.now()
print(x)

# ==========================================================================================================
# Maths Module -> min() , max() , abs() and pow() are built-in function.
#                 some functions of maths module -> (a) math.sqrt() -> square root 
#                                                   (b) math.ceil() ->  math.ceil(1.4) => return 2
#                                                   (c) math.floor() -> math.floor(1.4) => return 1
#                                                   (d) math.pi -> x = math.pi => x = 3.14..
#                 More about maths function:-  https://www.w3schools.com/python/module_math.asp
# ==========================================================================================================

import math

print(math.sqrt(4))
print(math.ceil(1.5))
print(math.floor(1.5))
print(math.pi)


# ==========================================================================================================
# RegEX Module -> Regular Expression, forms a  search Pattern.
#                 (1)findall-> Returns a list containing all matches and  if dont exist, list is empty
#                 (2)search-> Returns a first occurence Match object 
#                 (3)split -> Returns a list where the string has been split at each match
#                 (4)sub -> Replaces one or many matches with a string
#                 (5)compile -> compile a regular expression pattern string into a regex pattern object    
# ==========================================================================================================
import re

txt = "The rain in rain but the rain is in the rain"
x = re.split("rain", txt)
print(x)

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
x = re.search("rain", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

str = "432-123-4567"
pho_pat = re.compile('^\d{3}-\d{3}-\d{4}')
if pho_pat.match(str):
    print("Phone numbe is right")


# ==========================================================================================================
# OS module -> To have interaction with the Operating System.
#              
# ==========================================================================================================


# ==========================================================================================================
# ==========================================================================================================
# [MORE TO ADD]
# ==========================================================================================================
# ==========================================================================================================
