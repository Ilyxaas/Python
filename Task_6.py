


class Calc:

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def dell(a, b):
        return a / b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def pros(a, b):
        return a % b

    @staticmethod
    def dell2(a, b):
        return a // b

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Calc.sum(5, 5))
    print(Calc.dell(5, 5))
    print(Calc.dell2(5, 5))
    print(Calc.pros(5, 5))
    print(Calc.minus(5, 5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
