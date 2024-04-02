import os
arr = [1,2,3,4,5,6,7,8,9,10]

filepath = r"C:\Users\Администратор\Desktop\PP2_labs\lab6\Built-in_functions\5.py"

with open(filepath, 'a') as f:
    for i in arr:
        f.write(str(i))
    f.write("\n")
12345678910
