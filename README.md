# Defolderize
Copies all files in (direct) sub-folders of a given directory to the directory itself.

## Usage
`python defolderize.py path_to_main_directory`

Copies all files in direct sub-folders of the given main directory to the
main directoy itself. The file names of the copied files are prefixed 
with the name of the sub-folder plus "_".

## Example
`python defolderize.py c:\temp\images"`

All files in direct sub-folders of "c:\temp\images" will be copied
to "c:\temp\images". E.g. a file with the path "c:\temp\images\day_1\pic1.jpg"
will be copied to "c:\temp\images\day_1_pic1.jpg".
Files in "c:\temp\images\day_1\presentation" won't be copied.
