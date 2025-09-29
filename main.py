import webbrowser
from time import sleep
from colorama import Fore, Back, Style
from sys import exit
usernamelist = ["developer", "NOVAUSER"]
while True:
    username = input("Enter login:  ")
    if username in usernamelist:
        print("Checking...")
        sleep(1.5)
        print()
        break
    else:
        print("Checking...")
        sleep(1.5)
        print("Invalid login")
if username == "developer":
    truepassword = "deVLog301"
elif username == "NOVAUSER":
    truepassword = "NoVaUsEErr1913"
while True:
    password = input("Enter password:  ")
    if password == truepassword:
        print("Checking...")
        sleep(1.5)
        print("Welcome to VoidCLI, " + username + "!")
        break
    else:
        print("Checking...")
        sleep(1.5)
        print("Invalid password")
sleep(1)
print(Fore.LIGHTGREEN_EX + """
 _    _     _     _   
| |  | |   (_)   | |  
| |  | |__  _  __| |  
| |  | '_ \| |/ _` |  
| |__| | | | | (_| |  
 \____|_| |_|_|\__,_|  
      CLI
""")
with open('help.txt', 'r') as file:
    commandhelp = file.read()
while True:
    command = input(Fore.LIGHTRED_EX + "[" + username + "@localhost]: " + Fore.RESET)
    if command == "exit":
        exit()
        break
    elif command == "help":
        print(commandhelp)
    elif command == "about":
        print("it's not a serious project, it's similar to Linux, but the code is completely mine")
    elif command == "about -ru":
        print("это не серьезный проект, он похож на Linux, но код полностью мой")
    elif command == "about -fr":
        print("ce n'est pas un projet sérieux, c'est comme Linux, mais le code est entièrement à moi")
    elif command == "github":
        webbrowser.open('https://github.com/w1ux/VoidCLI')
    elif command == "browser":
        webbrowser.open('https://www.google.com')