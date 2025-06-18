# Porta Backup
 Porta Backup is a simple Python program that allows you to copy files from one place to another. The intended use is for one to use a USB flash drive to back up specific directories containing lightweight files that are frequently updated (e.g., notes, emails, small videos, etc.). This is not dissimilar to many of the automated cloud-based storage-solutions that conglomerates like Google, Amazon, and Microsoft offer. However, rather than incurring a monthly cost and requiring an internet connection, Porta Backup is essentially free and works completely offline.


## Installation

1. Download and extract the zip file containing this GitHub repository.
2. Open terminal and navigate to the directory containing the extracted repository.
3. Using `python3`, execute main.py. 

The program should be running now.


## Functionality

Updatee: the directory being updated.
Updater: the directory containing the files used for updating updatee.

I anticipate creating adjustable parameters for the program's functionality in the near future, but for the time being, the program functionally runs the same every time:

- FILES PRESENT IN THE UPDATEE'S DIRECTORY THAT AREN'T IN THE UPDATER'S DIRECTORY WILL BE DELETED
- FILES PRESENT IN THE UPDATER'S DIRECTORY THAT AREN'T IN THE UPDATEE'S DIRECTORY WILL BE CREATED
- FILES THAT ARE PRESENT IN BOTH WILL BE EVALUATED TO SEE IF THEY'RE IDENTICAL (the evaluation method is subject to change); IF THEY ARE DIFFERENT, THE UPDATEE'S FILL WILL BE REPLACED WITH THE UPDATER'S FILE OF THE SAME NAME.

