import os

folder_name = "student_data"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully.")
else:
    print("Folder already exists.")