import os
import glob

path = os.getcwd()    #The folder path to find the file

files = [f for f in glob.glob(path + "/Sample*.py", recursive=True)]       #the file type can be change

A = open("file.csv","w+")      #The name of the text file can be change

for f in files:

    #print(f)     
    os.system(f)   #run the file 
    June = os.popen(f).read()
    A.write(June)  #save it

         
A.close()