

def swapNums1(num1, num2):
    """
    Function to swap two numbers
    using a temporary variable
    """
    # Printing numbers before swapping
    print("Before Swapping:")
    print("num1: " , num1 , ", num2: " , num2)
    # Swapping with the help of a
    # temporary variable "temp"
    temp = num1
    num1 = num2
    num2 = temp
    # Printing numbers after swapping
    print("After Swapping:")
    print("num1: " , num1 , ", num2: " , num2)


def swapNums2(num1, num2):
    """
    Function to swap two numbers
    using arithmetic operators (+, -)
    """
    # Printing numbers before swapping
    print("Before Swapping:")
    print("num1: " , num1 , ", num2: " , num2)
    # Swapping with the help of
    # arithmetic operators (+, -)
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    # num1 = num1 * num2
    # num2 = num1 /num2
    # num1 = num1 / num2

    # Printing numbers after swapping
    print("After Swapping:")
    print("num1: " , num1 , ", num2: " , num2)


def swapNums3(num1, num2):
    """
    Function to swap two numbers
    using XOR operator
    """
    # Printing numbers before swapping
    print("Before Swapping:")
    print("num1: " , num1 , ", num2: " , num2)
    # Swapping with the help of
    # XOR operator
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    # Printing numbers after swapping
    print("After Swapping:")
    print("num1: " , num1 , ", num2: " , num2)


def swap_nums4(num1, num2):
    print("Before Swapping:")
    print("num1: " , num1 , ", num2: " , num2)
    # One line solution to swap two numbers
    num1, num2 = num2, num1
    print("After Swapping:")
    print("num1: " , num1 , ", num2: " , num2)


# Driver Code

#swapNums2(80, 50)
swap_nums4(80,50)