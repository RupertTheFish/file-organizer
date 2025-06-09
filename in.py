import os
import shutil

def organize_files(directory):
    # Define categories and their corresponding extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Pdfs": [".pdf"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Others": []
    }

    # Create reverse lookup for file extensions
    extension_to_category = {}
    for category, extensions in file_categories.items():
        for ext in extensions:
            extension_to_category[ext] = category

    # Organize files in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip directories and specific .py files
        if os.path.isdir(item_path):
            continue
        if item == "in.py" or item == "out.py":
            continue
        # Determine file extension
        _, ext = os.path.splitext(item)

        # Determine category
        category = extension_to_category.get(ext.lower(), "Others")

        # Create category folder if not exists
        category_folder = os.path.join(directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Move file to category folder
        # Calls for two arguments, the source and the destination
        shutil.move(item_path, os.path.join(category_folder, item))
# Specify the directory to organize
folder_to_organize = os.getcwd()
organize_files(folder_to_organize)
