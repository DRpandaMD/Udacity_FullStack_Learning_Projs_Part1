import os
import string
def renameFiles():
    #1 get file names from a folder
    fileList = os.listdir("/Users/michaelzarate/Documents/workspace_FullStack/RenameFilesProj/prank")
    print(fileList)
    saved_path = os.getcwd()
    os.chdir("/Users/michaelzarate/Documents/workspace_FullStack/RenameFilesProj/prank")

    #2 for each file rename the file
    for file_name in fileList:
        print("Old Name: " + file_name)
        print("New Name: " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)
    pass


renameFiles()
