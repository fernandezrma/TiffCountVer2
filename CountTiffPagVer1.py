''' This program counts pages of a group of .tiff image files in a given folder. 
It is mainly using the PyMuPDF library to accomplish the task.
The folder_path must be configured in the tiffFolderPath.json file that is
required to be included in the same folder where this program file resides. 
Also the syntax of tiffFolderPath.json has to be json.

Developed by: Miguel A. Fernandez under LGPL ver. 2 license.'''

import json
import fitz  # PyMuPDF library
import os

def count_tiff_pages_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out only TIFF files
    tiff_files = [f for f in files if f.lower().endswith(".tiff") or f.lower().endswith(".tif")]

    if not tiff_files:
        print("No TIFF files found in the folder.")
        return

    total_pages = 0
    total_tiff_files = 0

    print("TIFF pages count per .tiff file")
    print(f"Folder reviewed: {folder_path}")
    print("")
    for tiff_file in tiff_files:
        tiff_file_path = os.path.join(folder_path, tiff_file)

        # Open the TIFF file
        pdf_document = fitz.open(tiff_file_path)

        # Get the number of pages in the TIFF file
        num_pages = pdf_document.page_count
        total_pages += num_pages
        total_tiff_files += 1

        # Close the TIFF file
        pdf_document.close()

        print(f"File: {tiff_file} has {num_pages} pages.")

    print("")
    print("Process Report:")
    print(f"Total TIFF files processed: {total_tiff_files}")
    print(f"Total Pages in Folder: {total_pages}")

if __name__ == "__main__":
    # Read the folder path from the configuration file
    with open("tiffFolderPath.json", "r") as config_file:
        config = json.load(config_file)
    
    # Assign folder_path variable
    folder_path = config.get("folder_path")
    # Check if folder_path is empty
    if folder_path is None:
        print("Folder path not found in the configuration file.")
    else:
        count_tiff_pages_in_folder(folder_path)
    
