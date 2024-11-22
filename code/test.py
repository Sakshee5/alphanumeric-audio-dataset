import os

# Specify the folder where the files are located
folder_path = 'audio/Addresses'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Split the filename by the dot to separate the extension
    name, extension = os.path.splitext(filename)
    
    # Split the name by underscores and take the first two parts
    parts = name.split('_')
    new_name = '_'.join(parts[:2])  # Keep only the first two parts
    
    # Get the full old file path and the new file path with the same extension
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, new_name + extension)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)

    print(f'Renamed: {filename} -> {new_name + extension}')
