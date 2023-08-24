import os
import re
import sys

def is_valid_filename(filename):
    # Define your enumeration list here
    enum_list = ["custdigit", "finance", "HR"]
    
    # Create a regex pattern using the enumeration list
    pattern = rf"^bmwfs-({'|'.join(enum_list)})-\w*$"
    
    return bool(re.match(pattern, filename))

def validate_files_in_path(path):
    for root, _, files in os.walk(path):
        for file in files:
            if not is_valid_filename(file):
                print(f"Error: Invalid filename '{file}' in path '{root}'.")

if __name__ == "__main__":
    path_to_check = sys.argv[1]
    validate_files_in_path(path_to_check)
