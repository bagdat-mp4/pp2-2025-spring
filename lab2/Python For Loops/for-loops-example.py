# Мынау 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Мынау 2
for x in "banana":
    print(x)

# Мынау 3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Мынау 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# Мынау 5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Мынау 6
for x in range(6):
    print(x)

# Мынау 7
for x in range(2, 6):
    print(x)

# Мынау 8
for x in range(2, 30, 3):
    print(x)

# Мынау 9
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Мынау 10
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# Мынау 11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Мынау 12
for x in [0, 1, 2]:
    pass
