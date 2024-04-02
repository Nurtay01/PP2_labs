import os

filepath = r"C:\Users\Администратор\Desktop\PP2_labs\lab6\Built-in_functions\4.py"

with open(filepath, "r") as f:
    count = 0
    for line in f:
        count += 1
    print(count)