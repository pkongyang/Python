import os

dirName = ["A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I"]
os.chdir('C:\\')

for i in dirName :
    os.makedirs(i)