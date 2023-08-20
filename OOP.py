# ==========================================================================================================
# Object Oriented Language
# ==========================================================================================================

# ==========================================================================================================
# Creating a Class -> A class is a blueprint or a template for creating objects. It defines the properties
#                     (attribute) and behavior(method) of the object in the class
# ==========================================================================================================

class MyClass:
  x = 5

# ==========================================================================================================
#Creating an object-> Object is an Unique Instance of a class. Here 'm' has become an instane of class
#                    'MyClass'. Using this, You  can call the method and behavior of the class for that
#                     for that instance.
# ==========================================================================================================

m = MyClass()
print(m.x) #output will come 5

# ==========================================================================================================
# __init__() -> The method __init__() in the class is a special method, which is the class constructor that
#               python calls when you initialize a new instance.
# ==========================================================================================================

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# ==========================================================================================================
# __str__() ->  function controls what should be returned when the class object is represented as a string.
#               Use Curly Brackets to import the self values.  the 'f' in the start allows the input of self.
# ==========================================================================================================

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name(AGE) :- {self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# ==========================================================================================================
# Self parameter -> Refers to the current instance of the class, and helps in accessing the data of the
#                   instance belonging to the class. Self points at the instance name created and declare
#                   its data as its property.
# ==========================================================================================================


# ==========================================================================================================
# Inheritance -> Allows us to define a class that can inherit  the property and methods of another class.
#                Parent class is the class being inherited from. and Child class is the class that inherits
#                from it. 
#                We have alerdy created a 'person' class and we want a 'boy' class that inherits their 
#                property.
# ==========================================================================================================

class boy(Person):
  def sleep(self):
    print("Sleeping")

b1 = boy("Truffle", 13)
print(b1)  #prints out the __str__() method in person class out
b1.sleep()

# ==========================================================================================================
# Points to remember : (a) If u add __init__() method in a child class. then it will no longer inherit the 
#                          Parent's __init__() method. To use parent's __init__(), u have to call it as 
#                          "Parent.__init__(self, arguments)" inside the child's __init__()
#                      (b) super() :- ???
# ==========================================================================================================

# ==============================================================================================================
# Python Iterators -> An iterator in Python is an object that is used to iterate over iterable objects like 
#                     lists, tuples, dicts, and sets.
#                     The iter() method is called for the initialization of an iterator. This returns an 
#                     iterator object. 
#                     The __next__() method also allows you to do operations, and must return the next item 
#                     in the sequence.
#                     For more examples & understanding: https://www.w3schools.com/python/python_iterators.asp
#                     
#                     For loops uses these two defined function to loop, when we initiate a "for i in mylist:", 
#                     the for function executes __iter__() that makes i equal to the 0th index of the list and 
#                     executes __next__() method to increase to 1st index and then so on.
#
#                     To prevent the interation from going on forever, we raise "StopIteration" statement.
# ==============================================================================================================

class Test:
 
    # Constructor
    def __init__(self, limit):
        self.limit = limit
 
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self): 
        self.x = 10
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value ofx
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
 
        # Else increment and return old value
        self.x = x + 1
        return x
 
# Prints numbers from 10 to 15
for i in Test(15):
    print(i)
 
# Prints nothing
for i in Test(5):
    print(i)

# ==========================================================================================================
# Polymorphism -> Polymorphism is often used in class methods, where we can have multiple classes with the 
#                 same method name.
#                 As per the example below, The child classes inherits the properties and methods from the
#                 parent class. The Car class is empty, but it inherits brand, model and move() from 
#                 vehicle class. The boat and Plant classes also inherits all 3 but the move()  method is 
#                  overridden by their own move() method.
# ==========================================================================================================

class Cources():
  def __init__(self, name, branch):
    self.name = name
    self.branch = branch
  def subject(self):
    print(self.name, " in CSE")
    

class cse(Cources):
  pass

class ECE(Cources):
  def subject(self):
    print(self.name, "is ECE")

class Mech(Cources):
  def subject(self):
    print(self.name, "Is Mech")

cse1 = cse("Bart", "CSE")
ece1 = ECE("Simp", "ECE")
Mech1 = Mech("Troy", "Mech")

for i in (cse1, ece1, Mech1):
   i.subject()


# ==========================================================================================================
# ==========================================================================================================
# [Will Add more if needed]
# ==========================================================================================================
# ==========================================================================================================

      
