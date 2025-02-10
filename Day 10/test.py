# To list the files in the folder using Exceptional handling

import os

folders = input("Please provide the list of folders name: ").split()

for folder in folders:
    
    try:
        files = os.listdir(folder)

    except FileNotFoundError:
        print("Please provide a valid folder name!")
        break
    except PermissionError:
        print("No access to this: " + folder)

    print("--- listing files for the folder: " + folder)


    for file in folder:
        print(file)

        