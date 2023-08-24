import re
import sys

def is_valid_filename(filename):
    # Define your enumeration list here
    enum_list = ["cust1", "cust2", "cust3"]
    
    # Create a regex pattern using the enumeration list
    pattern = rf"^bmwfs-({'|'.join(enum_list)})-\w*$"
    
    return bool(re.match(pattern, filename))

if __name__ == "__main__":
    filename = sys.argv[1]
    if not is_valid_filename(filename):
        print(f"Error: Invalid filename '{filename}'.")
        sys.exit(1)
