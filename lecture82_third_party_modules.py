import time
import os
import pandas

while True:
    if os.path.exists("Files/temps-today.csv"):
        with open("Files/temps-today.csv") as file:
            data = pandas.read_csv("Files/temps-today.csv")
            print(data.mean())
    else:
        print("File does not exitst.")
    time.sleep(10)