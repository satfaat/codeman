

def findSum(n):
    """
    implementation to find the sum of
    first n natural numbers using recursion
    Recursive function to find the sum of first n natural numbers
    """
    if n<=1:
        return n
    else:
        return n + findSum(n-1)


# TESTS
def test1():
    n1 = 5
    n2 = 7
    n3 = 6
    print("n1: ", n1)
    print("n2: ", n2)
    print("n3: ", n3)
    print("Sum of first ", n1, " natural numbers: ", findSum(n1))
    print("Sum of first ", n2, " natural numbers: ", findSum(n2))
    print("Sum of first ", n3, " natural numbers: ", findSum(n3))


# Driver Code
test1()