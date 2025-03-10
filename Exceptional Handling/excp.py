import os

folders = input("Please provide the list of folder names: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name!")
        break 
# use continue instead of break to continue the loop

    except PermissionError:
        print("No access to this: " + folder)
    else:
        print("--- Listing files for the folder: " + folder)
        for file in files:
            print(file)