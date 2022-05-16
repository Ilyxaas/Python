def Calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/":
        return a / b
    elif operation == "//":
        return a // b
    elif operation == "%":
        return a // b
    elif operation == "*":
        return a * b
    elif operation == "**":
        return a ** b
    else:
        print("Данной операции нет")
        return -1

if __name__ == '__main__':
    print(Calculator(2, 2, "+"))
    print(Calculator(2, 2, "-"))
    print(Calculator(2, 2, "**"))
    print(Calculator(2, 2, "***"))
    print(Calculator(2, 2, "//"))
    print(Calculator(2, 2, "/"))
    print(Calculator(Calculator(2, 2, "+"),
                     Calculator(Calculator(2,
                                           Calculator(2, 2, "+"), "+"), 2, "+")
                     , "%")
          )

