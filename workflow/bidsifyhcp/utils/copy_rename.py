import os
import shutil
import re

def copy_and_rename_files(source_dir, target_dir, file_list, target_subdir, rename_map=None):
    """
    Copies the specified files from the source directory (and its subdirectories)
    to the target subdirectory and renames them if a rename map is provided.
    """
    # Ensure the target subdirectory exists
    os.makedirs(target_subdir, exist_ok=True)

    # Track if any files are not found
    files_not_found = {file_name: True for file_name in file_list}

    # Search through all subdirectories in the source directory for the files
    for root, dirs, files in os.walk(source_dir):
        for file_name in file_list:
            if file_name in files:
                source_file = os.path.join(root, file_name)
                
                # Check if a rename map exists, and rename the file if needed
                if rename_map and file_name in rename_map:
                    file_name = rename_map[file_name]

                target_file = os.path.join(target_subdir, file_name)

                shutil.copy(source_file, target_file)
                print(f"Copied and renamed {file_name} from {source_file} to {target_file}")
                files_not_found[file_name] = False

    # If any files were not found, print an error message
    for file_name, not_found in files_not_found.items():
        if not_found:
            print(f"Error: {file_name} not found in any subdirectory of {source_dir}")
