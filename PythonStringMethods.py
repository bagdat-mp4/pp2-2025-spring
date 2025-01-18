# capitalize()
txt = "hello, world!"
print(txt.capitalize())  # Hello, world!

# casefold()
txt = "HELLO"
print(txt.casefold())  # hello

# center()
txt = "Python"
print(txt.center(20))  # '       Python       '

# count()
txt = "banana"
print(txt.count("a"))  # 3

# encode()
txt = "My name is Ståle"
print(txt.encode())  # b'My name is St\xc3\xa5le'

# endswith()
txt = "Hello, world!"
print(txt.endswith("world!"))  # True

# expandtabs()
txt = "H\te\tl\tl\to"
print(txt.expandtabs(4))  # 'H   e   l   l   o'

# find()
txt = "Hello, world!"
print(txt.find("world"))  # 7

# format()
txt = "My name is {name}, I am {age} years old."
print(txt.format(name="John", age=30))  # My name is John, I am 30 years old.

# format_map()
data = {"name": "John", "age": 30}
txt = "My name is {name}, I am {age} years old."
print(txt.format_map(data))  # My name is John, I am 30 years old.

# index()
txt = "Hello, world!"
print(txt.index("world"))  # 7

# isalnum()
txt = "Hello123"
print(txt.isalnum())  # True

# isalpha()
txt = "Hello"
print(txt.isalpha())  # True

# isascii()
txt = "Hello!"
print(txt.isascii())  # True

# isdecimal()
txt = "12345"
print(txt.isdecimal())  # True

# isdigit()
txt = "12345"
print(txt.isdigit())  # True

# isidentifier()
txt = "variable1"
print(txt.isidentifier())  # True

# islower()
txt = "hello"
print(txt.islower())  # True

# isnumeric()
txt = "12345"
print(txt.isnumeric())  # True

# isprintable()
txt = "Hello\n"
print(txt.isprintable())  # False

# isspace()
txt = "   "
print(txt.isspace())  # True

# istitle()
txt = "Hello World"
print(txt.istitle())  # True

# isupper()
txt = "HELLO"
print(txt.isupper())  # True

# join()
my_list = ["Hello", "World"]
print(" ".join(my_list))  # Hello World

# ljust()
txt = "Hello"
print(txt.ljust(10))  # 'Hello     '

# lower()
txt = "HELLO"
print(txt.lower())  # hello

# lstrip()
txt = "   Hello"
print(txt.lstrip())  # 'Hello'

# maketrans() and translate()
txt = "Hello, World!"
my_table = txt.maketrans("H", "J")
print(txt.translate(my_table))  # Jello, World!

# partition()
txt = "I love Python"
print(txt.partition("love"))  # ('I ', 'love', ' Python')

# replace()
txt = "I love Python"
print(txt.replace("love", "like"))  # I like Python

# rfind()
txt = "Hello, world! Hello again!"
print(txt.rfind("Hello"))  # 14

# rindex()
txt = "Hello, world! Hello again!"
print(txt.rindex("Hello"))  # 14

# rjust()
txt = "Hello"
print(txt.rjust(10))  # '     Hello'

# rpartition()
txt = "I love Python. I love coding."
print(txt.rpartition("love"))  # ('I love Python. I ', 'love', ' coding.')

# rsplit()
txt = "apple, banana, cherry"
print(txt.rsplit(", "))  # ['apple', 'banana', 'cherry']

# rstrip()
txt = "Hello    "
print(txt.rstrip())  # 'Hello'

# split()
txt = "apple, banana, cherry"
print(txt.split(", "))  # ['apple', 'banana', 'cherry']

# splitlines()
txt = "Hello\nWorld"
print(txt.splitlines())  # ['Hello', 'World']

# startswith()
txt = "Hello, world!"
print(txt.startswith("Hello"))  # True

# strip()
txt = "   Hello   "
print(txt.strip())  # 'Hello'

# swapcase()
txt = "Hello, World!"
print(txt.swapcase())  # hELLO, wORLD!

# title()
txt = "hello world"
print(txt.title())  # Hello World

# translate()
txt = "abc"
my_table = str.maketrans("a", "z")
print(txt.translate(my_table))  # zbc

# upper()
txt = "hello"
print(txt.upper())  # HELLO

# zfill()
txt = "42"
print(txt.zfill(5))  # 00042
