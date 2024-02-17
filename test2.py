d = [
    {"name": "ASD1", "age": 18},
    {"name": "ASD2", "age": 18},
    {"name": "ASD3", "age": 19},
    {"name": "ASD4", "age": 20}
]
count = 0
for name in d:
    if name.get("age") == 19:
        count += 1
print(count)