


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        if i != 3 and i != len(s):
            if s[i] == "c" or s[i] == "с":
                print("Элемент номер ", i, " - с")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
