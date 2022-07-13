from time import sleep
from pathlib import Path
# project initialization
# print("loading", end="")
# for i in range(3):
#     sleep(1)
#     print(".", end="")
# print()
# sleep(2)
# print("--FILE AND FOLDER SYSTEM MANAGEMENT INITIALIZED--")

while True:
    try:
        print("Choose Suitable Option")
        print("1. Create Directory\n2. Read Directory\n0. Exit App")
        n = int(input("Your Input: "))
        if n == 1:
            pathdir = input("Enter directory name/path: ")
            path = Path(pathdir)
            path.mkdir(exist_ok=False)
        elif n == 2:
            path = Path('')
            for i, v in enumerate(path.rglob("*")):
                print(f"{i+1}. {v}")
            access = input("enter file name to access: ")
            print("You Will ...")
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
