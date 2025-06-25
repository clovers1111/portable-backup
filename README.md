# PORTA BACKUP
 PORTA BACKUP is a simple Python program that allows you to sync files between a reference directory and an outdated directory. This avoids the issues that come with overwriting and copying entire directories, needing to manually remove outdated folders and files, duplicate object conflicts, replacement prompts, etcetera. 
 
 The intended use is for one to use a USB flash drive to back up specific directories containing lightweight files that are frequently updated (e.g., notes, emails, small videos, etc.). This is not dissimilar to many of the automated cloud-based storage-solutions that conglomerates like Google, Amazon, and Microsoft offer. However, rather than incurring a monthly cost and requiring an internet connection, PORTA BACKUP is essentially free and works completely offline.


## Instructions and Installation
>### Glossary:
>- Updatee: the directory being updated.
>- Updater: the directory containing the files and subdirectories used for updating Updatee.

**For the moment, both of the working directories' root-most subdirectories <ins>must share a name.**</ins> For example, if your Updater's directory was ```/home/user/Documents/mybackup/``` the Updatee directory's final subdirectory would need to look something like ```/folder/folder/mybackup```.

1. Download and extract the zip file containing this GitHub repository.
2. Open terminal and navigate to the directory containing the extracted repository.
3. Using `python3`, execute main.py. 
4. Type in the directory you would like to update (i.e., Updatee) **starting from the root directory**.
5. Type in the directory you would like to use to update Updatee (i.e., Updater).
6. Confirm your selection **carefully** - there is a non-zero chance you might delete your root directory.

If you fail to enter a valid directory in step 4 or 5, you will be immediately prompted to re-enter the respective directory.



## Functionality


I anticipate creating adjustable parameters for the program's functionality in the near future, but for the time being, the program functionally runs the same every time:

- FILES PRESENT IN THE UPDATEE'S DIRECTORY THAT AREN'T IN THE UPDATER'S DIRECTORY $\color{red}{\textsf{WILL BE DELETED}}$.
- FILES PRESENT IN THE UPDATER'S DIRECTORY THAT AREN'T IN THE UPDATEE'S DIRECTORY WILL BE CREATED.
- FILES THAT ARE PRESENT IN BOTH WILL BE EVALUATED TO SEE IF THEY'RE IDENTICAL (the evaluation method is subject to change); IF THEY ARE DIFFERENT, THE UPDATEE'S FILE WILL BE REPLACED WITH THE UPDATER'S FILE OF THE SAME NAME.

### Known issues
- Shortcuts are ambiguous (i.e., not defined as a folder or a file) to the default python libraries [os](https://github.com/python/cpython/blob/3.13/Lib/os.py) and [shutil](https://github.com/python/cpython/blob/3.13/Lib/shutil.py); therefore, shortcuts are not backed up and, upon hitting one, may terminate the program prematurely. (This may also apply to other obscure file objects.)


## Long-Term Goals
- Implementing a highly modular system for user-inputted parameters that would alter the behavior of the program.
- A user interface.
- Updating the README with videos.
- Integrate failsafes to avoid potential catastrophies.