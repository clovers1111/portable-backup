import os
import shutil
import hashlib
import array

from classes import Directory
from messages import *

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

        print("Please CAREFULLY check that the following input is correct:\n")
        print(f"You are updatee: \n {updatee}")
        print(f"Using the directory: \n {updater} \n")
        userInput = input("Input [y/N]: ")
        if userInput != "y":
            iterator = 0


    

def objectify(root_dir, workingDir):
    for dirpath, dirlist, filelist in os.walk(root_dir):
        workingDir.append(Directory(dirpath, filelist))



#create lists of directory objects
objectify(updater, dirUpdater)
print("")
objectify(updatee, dirUpdatee)
print("")

#loop that iterates and compares objects in a list
i = 0
for updater in dirUpdater:

    j = 0
    updater_substring = updater.directory.split(delimiter)
    if (updater_substring[len(updater_substring)-1] == ""):
        updater_substring.pop(len(updater_substring)-1)
    updater_end = updater_substring[len(updater_substring)-1]

    for updatee in dirUpdatee:

        updatee_substring = updatee.directory.split(delimiter) # V name comparison to end of path
        if (updatee_substring[len(updatee_substring)-1] == ""):
            updatee_substring.pop(len(updatee_substring)-1)
        updatee_end = updatee_substring[len(updatee_substring)-1]

        if updatee.directory[len(updatee.directory)-1:] == "*":
            print("Already traversed!")

        elif updater_end == updatee_end:
            print(f"Traversing through directories \n {updater_end} \n V^V^V^V \n {updatee_end}")
            updater.compareTo(updatee)
            dirUpdatee[j].directory += "*"
            j += 1

        else:
            print(f"{updater_end} does not match {updatee_end}!")
    i += 1
print("\nSuccessfully updated directories!")






