#To find file in the same folder and subfolder and save it in text file

import glob

path = 'T:\\'       #The folder path to find the file

files = [f for f in glob.glob(path + "**/*.xlsx", recursive=True)]       #the file type can be change

A = open("file.txt","w+")     #The name of the text file can be change

for f in files:
    
    print(f)     
    A.write(f+ '\n')
         
A.close()
