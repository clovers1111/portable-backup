import os
import shutil
import hashlib
import array

from classes import Directory
from messages import *
from functions import *

#variable declarations
updater = ""
updatee = ""
dirUpdater = []
dirUpdatee = []
delimiter = "/"
userInput = ""
iterator = 0

print(f"{welcome_message}")
print(f"{version}\n")

print(readme)
while userInput != "y":
    while iterator != 2:

        if iterator == 0:
            updatee = input("Please input the directory you intend on updating: ")
            dirlength = len(updatee)
            if updatee[dirlength-1:] != "/":
                updatee = updatee + "/"
            if updatee[:1] != "/":
                updatee = "/" + updatee

            if os.path.isdir(updatee):
                iterator += 1
            else:
                print(f"Error: {updatee} is not a valid directory.")
                break

        else:
            updater = input("Please input the reference directory: ")
            dirlength = len(updater)
            if updater[dirlength-1:] != "/":
                updater = updater + "/"
            if updater[:1] != "/":
                updater = "/" + updater

            if os.path.isdir(updater):
                iterator += 1
            else:
                print(f"Error: {updater} is not a valid directory.")
                break
        
    if iterator == 2:
        print(f"\n{warning}")
        print(f"{liability}\n")

        print("Please CAREFULLY check that the following input is correct:\n\n")
        print(f"You are updating: \n {updatee}")
        print(f"Using the directory: \n {updater} \n")
        userInput = input("\nInput [y/N]: ")
        if userInput != "y":
            iterator = 0




# Create lists of directory objects
objectify(updater, dirUpdater)
print("")
objectify(updatee, dirUpdatee)
print("")

# Loop that iterates and compares directory objects in a list.
# This is segregated from the Directory class since we are iterating through an
#array of objects with array data members and need to discriminate the scope of 
#iteration between the array of objects and the array data member inside each object.
i = 0
for updater in dirUpdater:
    # Enumeration is necessary to correctly alter properties of the objects inside of the lists.
    j = 0

    # Creates an array of words and isolates the final word from the array (the working directory).
    updater_end = grabEnd(updater.directory)

    for updatee in dirUpdatee:

        # See precedent comment.
        updatee_end = grabEnd(updatee.directory)

        # If updatee ends with "*", it has been marked as complete.
        if updatee.directory[len(updatee.directory)-1:] == "*":
            print(f"Already traversed /{updatee_end}! ")
            

        # If the end of the arrays are identical, traverse both directories.
        elif updater_end == updatee_end:
            print(f"\nTraversing through directories \n /{updater_end} \n ↕↕↕↕↕↕↕↕↕↕↕↕ \n /{updatee_end}\n")
            updater.compareTo(updatee)
            dirUpdater[i].directory += "*" #marks as competed
            dirUpdatee[j].directory += "*" 

        else:
            print(f"/{updater_end} does not match /{updatee_end}!")
        j += 1
    i += 1

# Time to destroy entire directories
j = 0
for updatee in dirUpdatee:
    if updatee.directory[len(updatee.directory)-1:] != "*":
        print(f"{updatee.directory} does not exist in updater's directory. \n Deleting . . .")
        try:
            shutil.rmtree(updatee.directory)
        except FileNotFoundError:
            print(f"{updatee.directory} was a subdirectory of a previously deleted directory. \n")

        dirUpdatee[j].directory += "*"

# Each updater directory that hasn't been marked as having been traversed,
#the directory must not exist in the updatee's respective directory. We
#must match the highest common directory between the updater and the updatee
#to isolate and properly apply the subdirectories. By default, <os.walk> 
#starts at the highest common directory; we will use that to our advantage.

hcsd_updater = grabEnd(dirUpdater[0].directory)

updatee_list = dirUpdatee[0].directory.split(delimiter)
updatee_list = cleanUp(updatee_list)

updater_list = dirUpdater[0].directory.split(delimiter)
updater_list = cleanUp(updatee_list)

# Index number for hcsd_updater
updaterIN = len(updater_list)-1


# Chopping off everything after the first identical directory instance between
#directories.
i = 0
for subdir in updatee_list:
    if subdir == hcsd_updater:
        del updatee_list[i+1:]
        continue
    i += 1
# List that contains all of folders up until the shared folder in chronological
#order -- INCLUDING the shared folder between updater and updatee.
hcd_updatee = updatee_list

i = 0
for updater in dirUpdater:
    # At the end of the directory, if there isn't a "finished" (*) label --
    if updater.directory[len(updater.directory)-1:] != "*":
        #we need to create the new directory.
        temp_updater_list = listify(updater.directory)

        # All of the subdirectories of updater except the last 
        # shared folder between updater and updatee.
        upper = temp_updater_list[updaterIN+1:]

        new_dir_path = frankenDir(hcd_updatee, upper)
        print(f"Directory {new_dir_path} doesn't exist.")

        os.mkdir(new_dir_path)

        print(f"{new_dir_path} created!")
        print(f"Copying files . . .")

        for file in updater.filelist:
            updater.replFile(dirUpdater[i].directory, file, new_dir_path)
    i += 1
    

print("\nSuccessfully updated directories!")