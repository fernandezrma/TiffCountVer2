# TiffCountVer2
Program meant to count pages of multipage .tiff files in any given folder.

This program counts pages of a group of .tiff image files in a given folder. 
It is mainly using the PyMuPDF library to accomplish the task.
The folder_path must be configured in the tiffFolderPath.json file that is
required to be included in the same folder where this program file resides and runs. 
Also the syntax of tiffFolderPath.json has to be json.
The idea is to add the correct folder path inside the coresponding qoutes after
the folder_path variable of that file.
