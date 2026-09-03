import os

name = input("Enter file or folder name: ")

if os.path.exists(name):
    print("It exists.")
else:
    print("It does not exist.")