import json

# some JSON:
json_str =  '{ "name":"John", "age":30, "city":"New York"}'
py_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

def jsonToPy(str):
    parse = json.loads(str)
    print(parse["age"]) 
jsonToPy(json_str)

def pyToJson(str):
    convert = json.dumps(str)
    print(convert)
pyToJson(py_dict)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
