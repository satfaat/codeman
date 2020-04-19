'''
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc() # python is fantastic

print ("python is " + x) # python is awesome

# the global keyword
'''

def func():
    global x
    x = "global scope"

func()

print ("python is " + x)