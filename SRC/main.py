from functions import *
from variables import *
import os, time
import getpass

getpass.getpass(f" _    _ _                                    ______            __             \n| |  / (_)___ ____  ____  ___  ________     / ____/_  ______  / /_  ___  _____\n| | / / / __ `/ _ \/ __ \/ _ \/ ___/ _ \   / /   / / / / __ \/ __ \/ _ \/ ___/\n| |/ / / /_/ /  __/ / / /  __/ /  /  __/  / /___/ /_/ / /_/ / / / /  __/ /    \n|___/_/\__, /\___/_/ /_/\___/_/   \___/   \____/\__, / .___/_/ /_/\___/_/     \n      /____/                                   /____/_/    \n\n\nPresiona 'Enter'")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    option = getpass.getpass("[-    Menu    -]\n\t1) Cypher Text\n\t2) Decypher Text\n\t3) Exit")
    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Cypher\n")
        Cypher()
    elif option == "2":
        print("Decypher")
        pass
    elif option == "3":
        exit(1)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Wrong Option")
        time.sleep(3)
        pass