import os
import shutil
import hashlib
import array

from classes import Directory
from messages import *

def objectify(root_dir, workingDir):
    for dirpath, dirlist, filelist in os.walk(root_dir):
        workingDir.append(Directory(dirpath, filelist))

def grabEnd(dirtemp):
    dirtemp_list = listify(dirtemp)
    if dirtemp_list[len(dirtemp_list)-1] == "*":
        return dirtemp_list[len(dirtemp_list)-2]
    else:
        return dirtemp_list[len(dirtemp_list)-1]

def cleanUp(dirlist):
    if (dirlist[len(dirlist)-1] == ""):
        dirlist.pop(len(dirlist)-1)
    if dirlist[0] == "":
        dirlist.pop(0)
    return dirlist


def listify(dirtemp):
    dirtemp_list = dirtemp.split(delimiter)
    dirtemp_list = cleanUp(dirtemp_list)
    return dirtemp_list

def hCD(hcsd, dirtemp_list):
    for subdir in dirtemp_list:
        if subdir == hcsd:
            del dirtemp_list[i+1:]
    hcd_temp = delimiter.join(updatee_list)

def frankenDir(lower, upper):
    lower_combined = delimiter.join(lower)
    upper_combined = delimiter.join(upper)
    new_dir = "/" + lower_combined + "/" + upper_combined
    return new_dir