import os

filepath = r"C:\Users\Администратор\Desktop\PP2_labs\lab6\Built-in_functions\3.py"

if os.path.exists(filepath):
    print(os.path.split(filepath))