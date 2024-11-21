"""
This code matches airfoil file with its polar file and stores both airfoil and its polar in a new directory
Author: Sharath Hegde
Date: 2024-08-27 20:12:21
"""

import os
import re
import shutil

# dir paths
coordinates_database = "airfoil_coordinate_database"
polars_database = "airfoil_polar_database_csv"
combined_database = "combined_database_new"

# Ensure the output dir exists
os.makedirs(combined_database, exist_ok=True)

# lists of files in each dir
coord_files = [f for f in os.listdir(coordinates_database) if f.endswith('_coordinates.dat')]
polar_files = [f for f in os.listdir(polars_database) if f.endswith('.csv')]

# Extract base names from coordinate files
coord_bases = {re.sub(r'\_coordinates.dat$', '', f) for f in coord_files}
# print(coord_bases)
# mapping for polar files

polar_bases = {}
for polar_file in polar_files:
    match = re.match(r'xf-(.*)-il-1000000\.csv$', polar_file)
    if match:
        base_name = match.group(1)
        polar_bases[base_name] = polar_file

# print(polar_bases)

# Create the output directory structure
for base_name in coord_bases:
    if base_name in polar_bases:
        coord_file = f"{base_name}_coordinates.dat"
        polar_file = polar_bases[base_name]
        
        # Copy files into the output dir
        shutil.copy(os.path.join(coordinates_database, coord_file), combined_database)
        shutil.copy(os.path.join(polars_database, polar_file), combined_database)
        print(f"Copied {coord_file} and {polar_file} to {combined_database}")
    else:
        print(f"Warning: No polar file found for {base_name}")

print("File organization complete.")
