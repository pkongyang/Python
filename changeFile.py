import os
 
os.chdir('T:\\photo')  # directory
files = os.listdir(os.curdir)
for file in files:
    if '.png' in file:  # old file type
        newfile = file.replace('.png', '.jpg')   # old file type,new file type
        os.rename(file, newfile)