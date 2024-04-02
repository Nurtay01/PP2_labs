import os
char = "A"
while char <= "Z":
    filepath = r"C:\Users\Администратор\Desktop\PP2_labs\lab6\Built-in_functions\6.py" + char + ".txt"
    with open(filepath, "w") as f:
        f.close()
    char = chr(ord(char) + 1)