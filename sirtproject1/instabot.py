from time import sleep
from getpass import getpass
from instaBot import Bot
my_bot = Bot()

# introduction to app
# print("--WELCOME TO INSTABOT CLI APPLICATION--")
# sleep(2)
# print("setting up the connection with https://www.instagram.com/", end="")
# for i in range(3):
#     sleep(1)
#     print('.', end="")
# print()
# sleep(2)
# print("Connection established!")

# login user
username = input("username: ")
password = getpass(prompt="password: ")
my_bot.login(username=username, password=password)
