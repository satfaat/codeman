# getting the data type

x = 5
y = 1j # complex

print(type(x))

print(type(20.5))
print(type(y))
print(type(["apple", "banana"])) # list
print(type(("apple", "banana"))) # tuple
#print(type(range(6))

print(type({"name" : "John", "age" : 36})) # dict
print(type({"apple", "banana", "cherry"})) # set
print(type(frozenset({"apple", "banana", "cherry"}))) # frozenset
print(type(True)) # bool
print(type(b"Hello")) # bytes
print(type(bytearray(5))) # bytearray
print(type(memoryview(bytes(5)))) # memoryview