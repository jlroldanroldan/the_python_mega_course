import time

while True:
    with open("Files/vegetables.txt") as file:
        time.sleep(2)
        print(file.read())