import os
import shutil

# Directory
directory = r'C:\Users\venxer\Downloads'

# File type categories and their corresponding extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

# Creating subdirectories if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Moving files to their respective subdirectories
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                break

print("File organization complete!")