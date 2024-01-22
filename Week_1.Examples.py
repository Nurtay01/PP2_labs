# HOME
#example 1
print("Hello, World!")

# SYNTAX
#example1
if 5 > 2:
  print("Five is greater than two!")

# COMMENTS
#example 1
#This is a comment.

#example 2
print("Hello, World!") #This is a comment.

#example 3
#print("Hello, World!")

#example 4
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# VARIABLES
#example 1
x = 5
y = "John"
print(x)
print(y)

# example 3
x = str(3)
print(x)

#example 4
x = 5
print(type(x))

#example 5
x = "John"
print(x)
x = 'John'
print(x)

# Variable names
# example 1
myvar = "John"
my_var = "John"
print(myvar)
print(my_var)

# Variables - Assign Multiple Values
# example 1
x, y, z = "Orange", "Banana"
print(x)
print(y)

# example 2
x = y = z = "Orange"
print(x)
print(y)

# example 3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)

# Output Variables
# example 1
x = "Python is awesome"
print(x)

# example 2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# example 3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# example 4
x = 5
y = 10
print(x + y)

# example 5
x = 5
y = "John"
print(x, y)

# Global Variables
# example 1
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

#example 3
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# example 4
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# DATA TYPES
# example 1
x = 5
print(type(x))
# example 2
x = "Hello World"
print(type(x)) 

x = 20
print(type(x)) 

x = 20.5
print(type(x ))

x = 1j
print(type(x)) 

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x)) 

x = range(6)
print(type(x)) 

x = {"name" : "John", "age" : 36}
print(type(x)) 

x = {"apple", "banana", "cherry"}
print(type(x)) 

x = frozenset({"apple", "banana", "cherry"})
print(type(x)) 

x = True
print(type(x)) 

x = b"Hello"
print(type(x)) 

x = b"Hello"
print(type(x)) 

x = memoryview(bytes(5))
print(type(x)) 

x = None
print(type(x)) 

# NUMBERS
# example 1
x = 1    # int
print(x)

# example 2
x = 1    # int
a = float(x)
print(a)
print(type(a))

# example 3
import random
print(random.randrange(1, 10))

#CASTING
# example 1
x = 1
print(float(x))

# STRING
# example 1
a = "Hello, World!"
print(a[1])

# example 2
for x in "banana":
  print(x)
  
# example 3
a = "Hello, World!"
print(len(a))

# example 4
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Slicing strings
# example 1
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])

# Modify strings
# example 1
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Format strings
# example 1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Escape characters
# example 1
txt = "We are the so-called \"Vikings\" from the north."