

def reverseString1(str):
    """
    Python implementation to reverse a string
    using extended slice syntax
    """
    return str[::-1]


def reverseString2(str):
    """
    Python implementation to reverse a string
    using recursion
    """
    if len(str) == 0:
        return str
    else:
        return reverseString2(str[1:]) + str[0]


def reverseString3(str):
    """
    Python implementation to reverse a string
    using reversed method()
    """
    str = "".join(reversed(str))
    return str


def reverseString4(str):
    """
    Python implementation to reverse a string
    using a temporary string
    """
    tempStr = ""
    for s in str:
        tempStr = s + tempStr
    return tempStr


# Variables
def vars():
    str = [
        "MUO",
        "Welcome to MUO",
        "She sells seashells by the seashore"
    ]
    return str


# TESTS
def tst1():
    str = vars()
    print("Input string:")
    print(str[0])
    print(str[1])
    print(str[2])
    str1 = reverseString1(str[0])
    str2 = reverseString1(str[1])
    str3 = reverseString1(str[2])
    print("Reversed string:")
    print(str1)
    print(str2)
    print(str3)


def tst2():
    str = vars()
    print("Input string:")
    print(str[0])
    print(str[1])
    print(str[2])
    str1 = reverseString2(str[0])
    str2 = reverseString2(str[1])
    str3 = reverseString2(str[2])
    print("Reversed string:")
    print(str1)
    print(str2)
    print(str3)


def tst3():
    str = vars()
    print("Input string:")
    print(str[0])
    print(str[1])
    print(str[2])
    str1 = reverseString3(str[0])
    str2 = reverseString3(str[1])
    str3 = reverseString3(str[2])
    print("Reversed string:")
    print(str1)
    print(str2)
    print(str3)


def tst4():
    str = vars()
    print("Input string:")
    print(str[0])
    print(str[1])
    print(str[2])
    str1 = reverseString4(str[0])
    str2 = reverseString4(str[1])
    str3 = reverseString4(str[2])
    print("Reversed string:")
    print(str1)
    print(str2)
    print(str3)


# RUN TESTS
tst4()
