

def input(stdin):
    operator_code = str(stdin)[1:4]
    try:
        return int(operator_code)
    except ValueError:
        print("Please, enter phone number")


if __name__ == "__main__":
    for n in range(pow(10, 10), pow(10, 11)-1):
        input_str = input(n)
        print(input_str)