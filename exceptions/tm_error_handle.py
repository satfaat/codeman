def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(0))


try:
    print(9+6)
except:
    print("error message")
finally:
    print("please restart")


try:
    C = 2 + B
except:
    print("B needs to be defined")
else:
    print(u"Added successfully! The result is %s"%(C))

try:
    C = 2 + B
except NameError as err:
    print(err, ":", "B needs to be defined, please")
else:
    print(u"Added successfully! The result is %s"%(C))


try:
    B = 5
    C = 2 + B
    D = float(6)
    F = 7/0
except NameError as err:
    print(err,":", "B needs to be defined, please")
except ValueError as val:
    print(val,":", "You can't convert that data")
except ZeroDivisionError as zeroerr:
    print(zeroerr,":", "You can't divide a number by zero")
else:
    print(u"Operation successfull! The results are: %s, %s, and %s"%(C, D, F))


class connectionError(RuntimeError):
   def __init__(self, value):
      self.value = value
try:
   raise connectionError("Bad hostname")
except connectionError as err:
   print(err.value)


class errors(Exception):
    pass
class sixFiveError(errors):
   def __init__(self, value, message):
      self.value = value
      self.message = message
try:
   raise sixFiveError(6-5,"This substraction is not allowed")
except sixFiveError as e:
   print("There was an error:", e.message)

# First call the base exception classes:
class errors1(Exception):
    pass
# Next, derive your own exception from the base class:
class FloatError(errors1):
   def __init__(self, value, message):
      self.value = value
      self.message = message
# Create a function to add two floats:
def addTwoFloat(a, b):
	if (type(a) and type(b)) != float:
		raise FloatError(a+b,"Numbers must be float to add")
	else:
		print(a + b)
addTwoFloat(4, 7)