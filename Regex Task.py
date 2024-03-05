import os
import shutil
import re

# Specify the main folder path
dir_path = input("Enter a directory path: ")

# Specify the new directory
new_dir_path = input("Enter the new directory path: ")

# Ensure the new directory exists
if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

# Specify the Regex pattern to match files that are not in English
regex_input = input("Enter the Regex: ")
pattern = re.compile(regex_input)
# The Regex: \w+_(?!en-[A-Z]{2}).*$

# A function to get all the paths of files
def get_file_paths(dir_path):
# A list to store file path
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            file_paths.append(os.path.join(root, name))
    return file_paths

# A function to move files to the new directory
def move_file(file_paths):
    for path in file_paths:
        #Get all the file names
        name = os.path.basename(path)
        # Check if the file name matches the pattern
        if pattern.search(name):        
            # Move the file to the new directory
            shutil.move(path, os.path.join(new_dir_path, name))

# Ensure all the files are included
print(get_file_paths(dir_path)) 
#Store all the file path
all_file_paths = get_file_paths(dir_path)
move_file(all_file_paths)
#Make sure all the files are moved to the new directory
print("Complete!")