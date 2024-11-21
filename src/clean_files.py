"""
Remove the unwanted spaces and characters in the airfoil coordinate file
Author: Sharath Hegde
Date: 25.08.2024
"""

import os
import tempfile

def filter_coordinates(input_file_path):
    # Create a temporary file for writing the filtered data
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', dir=os.path.dirname(input_file_path)) as temp_file:
        temp_file_path = temp_file.name
        
        with open(input_file_path, 'r') as infile, open(temp_file_path, 'w') as outfile:
            lines = infile.readlines()
            print("lines:", lines)
            # Discard the first two lines
            for line in lines[5:]:
                print("line:", line)
                parts = line.split()
                print("Parts:", parts)
                if len(parts) == 2:
                    try:
                        x = float(parts[0])
                        y = float(parts[1])
                        # Write the valid line to the temporary file
                        outfile.write(f"{x} {y}\n")
                    except ValueError:
                        # Skip lines where conversion to float fails
                        continue

    # Replace the original file with the filtered data
    os.replace(temp_file_path, input_file_path)

# Directory where files are saved
save_directory = "/" # provide a path

# Process each file in the directory
for filename in os.listdir(save_directory):
    if filename.endswith("_coordinates.dat"):
        input_path = os.path.join(save_directory, filename)
        filter_coordinates(input_path)

print("Coordinate files cleaned.")

