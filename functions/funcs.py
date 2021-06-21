def summ(num1, num2):
    summ = num1 + num2
    print(f'output {summ}')
    return summ

print(summ(5, 6))


out_of_def = "awesome"

def func1():
    out_of_def = "fantastic"
    print("Python is " + out_of_def)

func1() # python is fantastic
print("python is " + out_of_def) # python is awesome


# the global keyword
def func2():
    global x
    x = "global scope"

func2()
print ("python is " + x)


# tm local var
def spam():
    eggs = 99
    bacon()
    #eggs = bacon.eggs
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()