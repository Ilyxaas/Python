from collections import Counter

class FileManager:
    def __init__(self, s, type):
        self.File = open(s, type)

    def Close(self):
        self.File.close

    def Write(self, s):
        self.File.write(s)

    def TextToArray(self):
        return self.File.read().replace("\n", " ").split(" ")

    @staticmethod
    def TextToArray2 (s):
        return s.replace(" ").split(" ")


if __name__ == '__main__':
    s = "/Users/ilya/HomeWork/File_window/text"
    s1 = "/Users/ilya/HomeWork/File_window/Text_out"
    soyzi = ["и", "также", "но", "a", "когда", "да"]
    stopTask = "stop"
    fileinput = FileManager(s, 'r')
    Array = fileinput.TextToArray()
    b = [i for i in Array if i not in soyzi]
    c = Counter(b)
    val = max(c.values())

    for i in c.items():
        if i[1] == val:
            name = i[0]

    print("Максимальное кол-во повторений у слова - ", name)

    fl = True
    mass = []
    while fl:

        string = input()
        if string == stopTask:
            In = FileManager(s1, 'w')
            c1 = Counter(mass)
            st = ""
            for i in c1.items():
                st += "[" + str(i[0]) + " - " + str(i[1]) + "] "
            print(st)
            In.Write(st)
            break
        else:
            mass += string.split(", ")
            print(mass)


    print("Exit")

