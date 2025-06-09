import os
import shutil

def desorganize_files(directory):
    # Iterate through all files and folders in the main directory
    for root, dirs, files in os.walk(directory):
        # Skip the root directory itself (start processing subdirectories)
        if root == directory:
            continue

        # Move all files in the current subdirectory to the main directory
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, os.path.join(directory, file))

        # Remove the subdirectory after moving all its files
        for sub_dir in dirs:
            sub_dir_path = os.path.join(root, sub_dir)
            os.rmdir(sub_dir_path)

        # Once files are moved, remove the empty parent directory
        os.rmdir(root)

# Specify the directory to desorganize
folder_to_desorganize = os.getcwd()
desorganize_files(folder_to_desorganize)
