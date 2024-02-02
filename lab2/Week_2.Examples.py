# BOOLEANS
#example
print(10 > 9)
print(10 == 9)
print(10 < 9)
#example 2
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#example 3
print(bool("Hello"))
print(bool(15))
#example 4
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#examle 5
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
#example 6
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
# example 7
class myclass():
  def __len__(art):
    return 0
myobj = myclass()
print(bool(myobj))
# example 8
def myFunction() :
  return True
print(myFunction())
# example 9
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
# example 10  isinstance() - Check the integer for type 
x = 200                    
print(isinstance(x, int))

# OPERATORS
# example 1
print(10 + 5)
# example 2
x = 5
y = 3
print(x + y) #addition
print(x - y) #substraction
print(x * y) # multiplication
print(x / y) #division
print(x % y) #modulus
print(x ** y) #exponentation
print(x // y) #floor division

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

# LISTS
# example 1
thislist = ["apple", "banana", "cherry"]
print(thislist)
# example 2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# example 3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# example 4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
# example 5
list1 = ["abc", 34, True, 40, "male"]
print(list1)
# example 6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# example 7
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# Access List Items
# example 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# example 2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# example 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Change List Items
# example 1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# example 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# example 3   insert() - put an integer in given index
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
# Add List Items
# example 1 append() - put an integer at the end of a List
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# example 2  extend() - Add a List to another List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Remove List Items
# example 1  remove() - to delete an integer
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# example 2 pop() - delete integer in index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# example 3
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# example 4
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# Loop lists
# example 1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# example 2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
# example 3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
# example 4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# List Comprehension
# example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
# example 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# example 3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#example 4
newlist = [x for x in range(10)]
print(newlist)
# example 5
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# example 6
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
# example 7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# Sort Lists
# example 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# example 2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# example 3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# example 4
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# example 5
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 
# Copy Lists
# example 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# example 2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# Join Lists
# example 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# example 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
# example 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# TUPLES
# example 1
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# example 2
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
# example 3
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
# Accces tuples
# example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# example 2
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
# Update Tuples
# example 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# example 2
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
# example 3
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
# Unpack Tuples
# example 1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# example 2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
# Loop Tuples
# example 1
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# example 2
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# SETS
# example 1
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# Access Set Items
# example 1
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# Add Set Items
# example 1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# example 2   update() - add two sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# DICTIONARY
# example 1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# example 2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# example 3
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
# example 4
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
# example 5
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
# example 6
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
car["year"] = 2020
print(x)
# example 7  items() - dict to list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
car["year"] = 2020
print(x)
# Add Dictionary Items
# example 1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
# Remove Dictionary Items
# exampe 1   popitem() - delete last element
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# example 2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# Loop Dictionary
# example 1   
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
# example 2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

# IF ELSE 
# example 1
a = 33
b = 200
if b > a:
  print("b is greater than a")
# example 2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# WHILE LOOPS
# example 1
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
# example 2
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# FOR LOOPS
# example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
# example 2
for x in range(2, 30, 3):
  print(x) 
# example 3
for x in range(6):
  print(x)
else:
  print("Finally finished!")



 