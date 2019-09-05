import time
import os


while True:
    if os.path.exists("Files/vegetables.txt"):
        with open("Files/vegetables.txt") as file:
            time.sleep(2)
            print(file.read())
    else:
        print("File does not exitst.")
    time.sleep(10)

