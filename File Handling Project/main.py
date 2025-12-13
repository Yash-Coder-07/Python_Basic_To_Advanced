from pathlib import Path
import os
def readFileandFolder():
    path = Path('') # get the path of current folder
    items = list(path.rglob('*'))

    for i, items in enumerate (items):
        print(f"{i+1} : {items} ")


def createFile():
    try:

        readFileandFolder()
        name = input("Please tell your file name :")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in this file :")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")    
        else:
            print("This file is already createe")

    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readFileandFolder()
        name = input("Which file you want to read")
        p = Path(name) # if name exist then we get path else create path
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
        
            print("READED SUCCESSFULLY")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"An error is occured as {err}")


def updateFile():
    try:
        readFileandFolder()
        name = input("Which file you want to update")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of file")
            print("Press 2 for overwriting your file")
            print("Press 3 for appending the some content in your file")

            res = int(input("Tell ypur response: "))

            if res ==1:
                name2 = input("Tell me your name file")
                p2 = Path(name2)
                p.rename(p2)
        
            if res==2:
                with open(p,'w') as fs:
                    data = input("Tell what you want to overwrite data : ")
                    fs.write(data)
        
            if res==3:
                with open(p,'a') as fs:
                    data = input("What you want to write in data")
                    fs.write(data)
    except Exception as err:
        print(f"An error is occured {err} ")


def deleteFile():
    try:
        readFileandFolder()
        name = input("Which file you want to delete :")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File is successfully removed")
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")



print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for delete a file")

check = int(input("Please tell your response: "))

if(check==1):
    createFile()

if check==2:
    readfile() 

if check ==3:
    updateFile()

if check==4:
    deleteFile()