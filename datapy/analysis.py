

def see_type(var):
    # getting the data type
    print(type(var))


# Variables
x = 5
y = 1j # complex


# RUN FUNCTION
see_type(x)
see_type(20.5)
see_type(y)
see_type(["apple", "banana"])  # list
see_type(("apple", "banana"))  # tuple

#print(type(range(6))

print(type({"name" : "John", "age" : 36})) # dict
print(type({"apple", "banana", "cherry"})) # set
print(type(frozenset({"apple", "banana", "cherry"}))) # frozenset
print(type(True)) # bool
print(type(b"Hello")) # bytes
print(type(bytearray(5))) # bytearray
print(type(memoryview(bytes(5)))) # memoryview


x, y, z = "orange", "banana", "cherry"

x=y=z = "orange"

x = "python is "
y = "awesome"
z = x + y;
print(z)

# data types
'''
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
'''

# specify a variable type
x = int(2.8) # will be 2
y = float(1) # will be 1.0
z = str(2) # will be "2"

# multiline strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

#Arrays

#TUPLE кортеж
tuple() # ()

#LIST 
list() # []

# Словарь
dict() # {}

# SET множество
set() # {}