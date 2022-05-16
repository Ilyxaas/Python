# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


44

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = input()
    i = 0
    len = len(s)
    fl = False

    while (i < len):
        if (i != len and i != 3 ):
            if (s[i] == "c"):
               fl = True

        i = i + 1
    if (fl):
        print("есть элемент с")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
