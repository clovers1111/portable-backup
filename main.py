import os
import shutil
import hashlib
import array

#create replace file function
#create function for copying new files
#create function for deleting new files

# Hardcoded example file path *MUST END WITH A FORWARD SLASH*
#test is our updated reference; updatee is being updated
updater = "/home/harry/PycharmProjects/PythonProject/test/"
updatee = "/home/harry/PycharmProjects/PythonProject/test2/test/"
hash_algorithm = 'sha256'
hash_object = hashlib.new(hash_algorithm)

# Class that will hold all the relevant traits for comparison
class Directory:
    def __init__(self, directory, filelist):
        self.directory = directory
        self.filelist = filelist
        self.marker = []
        for file in filelist:
            self.marker.append(os.path.getmtime(directory + "/" + file))

        print(f"New class created from {directory}")

    #comparison based on name and then timemarker
    def compareTo(self, updatee):

        #variable declaration; keeps track of static comparison files
        i = 0
        #nested for loops to iterate and compare
        for file in self.filelist:
            j = 0 #starts from 0 after successful finds
            for filet in updatee.filelist:
                if file == filet: #names are the same
                    if self.marker[i] == updatee.marker[j]: #markers are the same
                        print(f"{file} is the same")
                        break
                    else:
                        print(f"{file} needs to be updated")
                        self.replFile(i,j)
                        self.checkFile(self.directory + file, updatee.directory + filet)
                        break
                j += 1
            i += 1
        return

    #check if the files updated correctly
    def checkFile(self, updater_file, updatee_file):
        if updater_file == updatee_file:
            return

    #replaces file based on file's index inside filelist
    def replFile(self, i, j):
        return
        


def objectify(root_dir, workingDir):
    for dirpath, dirlist, filelist in os.walk(root_dir):
        workingDir.append(Directory(dirpath, filelist))


#main

# variable declaration
dirUpdater = []
dirUpdatee = []
delimiter = "/"

#create lists of directory objects
objectify(updater, dirUpdater)
print("")
objectify(updatee, dirUpdatee)
print("")

#loop that iterates and compares objects in a list
for updated in dirUpdater:
    updated_substring = updated.directory.split(delimiter)
    for updating in dirUpdatee:
        updating_substring = updated.directory.split(delimiter) # V name comparison to end of path
        if updated_substring[len(updated_substring)-2] == updating_substring[len(updating_substring)-2]:
            updated.compareTo(updating)
print()






