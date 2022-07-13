from time import sleep
from pathlib import Path
import os

# project initialization
print("loading", end="")
for i in range(3):
    sleep(1)
    print(".", end="")
print()
sleep(2)
print("--FILE AND FOLDER SYSTEM MANAGEMENT INITIALIZED--")

while True:
    try:
        print("Choose Suitable Option")
        print("1. Create Directory\n2. Read Directory\n3. Update Directory\n4. Delete Directory\n5. Create File\n6. Read File Data\n7. Delete File\n8. Update File Data\n0. Exit App")
        n = int(input("Your Input: "))
        if n == 1:
            pathdir = input("Enter directory name/path: ")
            path = Path(pathdir)
            path.mkdir(exist_ok=False)
            print("-- FOLDER CREATED SUCCESSFULLY --")
        elif n == 2:
            path = Path('')
            for i, v in enumerate(path.rglob("*")):
                print(f"{i+1} . {v}")
            print("--  ABOVE LIST SHOWES ALL FILE AND FOLDER --")
        elif n == 3:
            pathdir = input("Enter directory name/path to be renamed: ")
            path = Path(pathdir)
            path.rename(input("New Folder Name: "))
            print("-- FOLDER RENAMED SUCCESSFULLY --")
        elif n == 4:
            pathdir = input("Enter directory name/path to be deleted: ")
            path = Path(pathdir)
            filefolderlist = [i for i in path.rglob("*")]
            if len(filefolderlist) > 0:
                ask = input(
                    "Folder is not empty, do you wnat to delete all files and folder ?(Y/N)")
                if ask == 'Y' or ask == "y":
                    for i in filefolderlist:
                        if i.is_file():
                            os.remove(i)
                        else:
                            path1 = Path(i)
                            path1.rmdir()
                else:
                    continue
            path.rmdir()
            print("-- FOLDER REMOVED SUCCESSFULLY --")
        elif n == 5:
            path = Path('')
            for i, v in enumerate(path.rglob("*")):
                print(f"{i+1}. {v}")
            print("--  AVAILABLE FOLDERS TO CREATE FILE --")
            pathdir = input("Enter file name/path to be created: ")
            if Path(pathdir).exists():
                raise Exception("File Already Present!")
            with open(pathdir, 'w') as f:
                text = input("Entre file data(press enter to skip): ")
                f.write(text)
            print("-- FILE CREATED SUCCESSFULLY --")
        elif n == 6:
            path = Path('')
            for i, v in enumerate(path.rglob("*.*")):
                print(f"{i+1}. {v}")
            print("-- TOTAL FILES PRESENT --")
            pathdir = input("Enter file name/path to be read: ")
            with open(pathdir, 'r') as f:
                print("FETCHED DATA >> ", f.read())
                print("-- FILE DATA ENDS --")
            print("-- FILE READ SUCCESSFULLY --")
        elif n == 7:
            path = Path('')
            for i, v in enumerate(path.rglob("*.*")):
                print(f"{i+1}. {v}")
            print("-- TOTAL FILES PRESENT --")
            pathdir = input("Enter file name/path to be read: ")
            ask = input("Do you want to delete this file ? (Y/N) ")
            if ask == 'y' or ask == 'Y':
                os.remove(pathdir)
                print("-- FILE DELETED SUCCESSFULLY --")
            else:
                print("-- DELETE OPERATION CANCELLED -- ")
        elif n == 8:
            path = Path('')
            for i, v in enumerate(path.rglob("*.*")):
                print(f"{i+1}. {v}")
            print("-- TOTAL FILES PRESENT --")
            ask = int(input(
                "1. For Renaming file\n2. For appending data\n3. For replacing the data\n Choose your option: "))
            pathdir = input("Enter file name/path to be read: ")

            if ask == 1:
                os.rename(pathdir, input("New File name directory: "))
                print("-- FILE RENAMED SUCCESSFULLY")
            elif ask == 2:
                with open(pathdir, 'r') as f:
                    print("FETCHED DATA >> ", f.read())
                    with open(pathdir, 'a') as fa:
                        newtxt = input("New Appending Data: ")
                        fa.write(f"\n{newtxt}")
                    print("-- New Data Appended --")
            elif ask == 3:
                with open(pathdir, 'r') as f:
                    print("FETCHED DATA >> ", f.read())
                    with open(pathdir, 'w') as fa:
                        newtxt = input("New Replacing Data: ")
                        fa.write(newtxt)
                    print("-- New Data Replaced --")
                print("-- UPDATING COMPLETED SUCCESSSFULLY --")
            else:
                print("-- WRONG INPUT CHOOSE AGAIN --")
        elif n == 0:
            print("loading", end="")
            for i in range(3):
                sleep(1)
                print(".", end="")
            print()
            print("App Closed!")
            break
        else:
            print("-- INVALID INPUT --")
    except Exception as err:
        print(err)
