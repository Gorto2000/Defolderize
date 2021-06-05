#------------------------------------------------------------------------------
# DEFOLDERIZE
# (c) 2021 Christopher Thiele
#
# Usage: python defolderize.py path_to_main_directory
#
# Copies all files in direct sub-folders of the given main directory to the
# main directoy itself. The file names of the copied files are prefixed 
# with the name of the sub-folder plus "_".
#
#------------------------------------------------------------------------------

import shutil
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("DEFOLDERIZE expects one argument: The path to a folder where its sub-folders shall be \"defolderized\".")
        return

    if sys.argv[1] == "--help" or sys.argv[1] == "/?" or sys.argv[1] == "-h":
        print("Usage: python defolderize.py path_to_main_directory")
        print("Copies all files in direct sub-folders of the given main directory to the main directoy itself.")
        print("The file names of the copied files are prefixed with the name of the sub-folder plus \"_\".")
        print("")
        print("Example: python defolderize.py c:\\temp\\images")
        print("         All files in direct sub-folders of \"c:\\temp\\images\" will be copied")
        print("         to \"c:\\temp\\images\". E.g. a file with the path \"c:\\temp\\images\\day_1\\pic1.jpg\"")
        print("         will be copied to \"c:\\temp\\images\\day_1_pic1.jpg\".")
        print("         Files in \"c:\\temp\\images\\day_1\\presentation\" won't be copied.")
        return

    if os.path.isdir(sys.argv[1]) == False:
        print("Error: \"" + sys.argv[1] + "\" is not a directory." )
        return

    subfolders = [ { "name": f.name, "path": f.path } for f in os.scandir(sys.argv[1]) if f.is_dir() ]
    for subfolder in subfolders:
        print("Copying files of sub-folder \"" + subfolder["name"] +"\"...")
        files = [ { "name": f.name, "path": f.path } for f in os.scandir(subfolder["path"]) if f.is_dir() == False ]
        for file in files:
            shutil.copy2(file["path"], sys.argv[1] + "/" + subfolder["name"] + "_" + file["name"])
    print("Done.")

if __name__ == '__main__':
    main()
