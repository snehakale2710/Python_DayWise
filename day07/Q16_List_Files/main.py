import os

print("Files and Folders:")

items = os.listdir()

for item in items:
    print(item)