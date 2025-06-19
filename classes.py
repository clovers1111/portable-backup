import os
import shutil
import array
import hashlib

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
                        print(f"{file} is the same.")
                        self.filelist[i] = file + "*"
                        updatee.filelist[j] = self.filelist[i]
                        break
                    else:
                        print(f"{file} needs to be updated.")
                        self.replFile(self.directory, file, updatee.directory)
                        self.filelist[i] = file + "*"
                        updatee.filelist[j] = self.filelist[i]
                        break
                j += 1
            i += 1
        #creates and deletes files depending on their respective presences
        self.checkDir(updatee)

    #check if the files updated correctly
    def checkFile(self, file_path, filet_path):
        print(f"Checking {filet_path} . . .")
        if os.path.getmtime(file_path) == os.path.getmtime(filet_path):
            print(f"Complete: file update successful from {file_path}! \n")
        else:
            print("Error: files likely failed to update.")
        return

    #see if the files in two directories match
    def checkDir(self, updatee):
        i = 0
        for file in self.filelist:
            fnamesize = len(file)
            while (file[fnamesize-1:] != "*"):
                print(f"{file} does not exist in updatee's directory.")
                self.replFile(self.directory, file, updatee.directory)
                self.filelist[i] = file + "*"
                updatee.filelist.append(self.filelist[i])
                break
            i += 1
        i = 0
        for filet in updatee.filelist:
            tnamesize = len(filet)
            while (filet[tnamesize-1:] != "*"):
                print(f"{filet} does not exist in updater directory.")
                self.delFile(updatee.directory, filet)
                updatee.filelist[i] = filet + "*"
                break
            i += 1
        return


    #function for file deletion            
    def delFile(self, filet_dir, filet):
        print(f"Deleting {filet} . . .")
        os.remove(filet_dir + "/" + filet)
        print(f"{filet} successfully deleted.")
        return

    #copies file info and metadata 
    def replFile(self, file_dir, file, filet_dir):
        #copies reference file to new file
        print(f"Updating {filet_dir} . . .")
        #get all subdirectories after the first match o
        shutil.copy2(file_dir + "/" + file, filet_dir + "/" + file)
        self.checkFile(file_dir + "/" + file, filet_dir + "/" + file)
        file = file + "*"
        return
    
    def findDir(self, file_dir, filet_dir):
        #find directory to make for new folder
        return