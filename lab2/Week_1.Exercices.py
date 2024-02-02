# BOOLEANS
# exercise 1
print(10 > 9)
True
# exercise 2
print(10 == 9)
False
# exercise 3
print(10 < 9)
False
# exercise 4
print(bool("abc"))
True
# exercise 5
print(bool(0))
False

# OPERATORS
# exercise 1
print(10*5)
# exercise 2
print(10/2)
# exercise 3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
# exercise 4
if 5 != 10:
  print("5 and 10 is not equal")
# exercise 5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

# LISTS
# exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# exarcise 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
# exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
# exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
# exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# exercise 6
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[3:6])
# exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:6])
# exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# TUPLES
# exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
# exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
# exercise 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#SETS
#exercise1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#exercise2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#exercise3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#exercise4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#exercise5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#DICTIONARY
#exercise1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#exercise2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020
#exercise3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
#exercise4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#exercise5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#IF_ELSE
#exercise1
a = 50
b = 10
if a>b:
    print("Hello World")
#exercise2
a = 50
b = 10
if a!=b: 
    print("Hello World")
#exercise3
a = 50
b = 10
if a==b:
    print("Yes")
else:
    print("No")
#exercise4
a = 50
b = 10
if a==b:
  print("1")
elif a>b:
  print("2")
else:
  print("3")
#exercise5
if a == b and c == d:
  print("Hello")
#exercise6
if a == b or c == d:
  print("Hello")
#exercise7
if 5 > 2:
    print("YES")
#exercise8
a = 2
b = 5
print("YES") if a == b else print("NO")
#exercise9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")
  
#WHILE_LOOP
#exercise1
i = 1
while i < 6:
    print(i)
    i += 1
#exercise2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
#exercise3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#exercise4  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
#FOR_LOOOOP
#exercise1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#exercise2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#exercise3
for x in range(6):
  print(x)
#exercise4  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)