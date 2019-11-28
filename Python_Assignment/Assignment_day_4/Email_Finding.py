import os.path
import re

pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


for d in list(filter(lambda dd: os.path.splitext(dd)[1] == ".log",os.listdir("C:\\Users\\tanga2\\PycharmProjects\\OOP\\Test"))):
    fo = open("C:\\Users\\tanga2\\PycharmProjects\\OOP\\Test" + "\\" + d, 'r')
    for line in fo:
        if re.search(pattern,line):
            print(line)

