

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = input()
    l = len(s) // 2
    fl = True
    for i in range(l):
        if s[len(s) - i - 1] != s[i]:
            fl = False
    if fl:
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
