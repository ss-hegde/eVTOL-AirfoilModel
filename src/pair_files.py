# %%
# This code randomly select a number of airfoil coordinates and the cooresponding polar files and copies them to a new folder.

# %%
import os
import random
import shutil

# %%
# Define the paths
coordinates_folder = './airfoil_database/airfoil_coordinate_database/'
polar_folder = './airfoil_database/airfoil_polar_database_csv/'
output_folder = './small_database_training_csv/'

# List the airfoil coordinate files
coordinate_files = [f for f in os.listdir(coordinates_folder) if f.endswith('_coordinates.dat')]

# Randomly select 200 airfoils
selected_airfoils = random.sample(coordinate_files, 200)

# %%
# Iterate over selected airfoils and copy both coordinate and polar files
for airfoil_file in selected_airfoils:
    # Define source and destination for the airfoil coordinate file
    airfoil_path = os.path.join(coordinates_folder, airfoil_file)
    destination_airfoil_path = os.path.join(output_folder, airfoil_file)

    # Copy the airfoil coordinate file to the new folder
    shutil.copy(airfoil_path, destination_airfoil_path)

    # Derive the corresponding polar filename
    airfoil_name = airfoil_file.replace('_coordinates.dat', '')  # Remove the '.dat' extension
    polar_filename = f'xf-{airfoil_name}-il-1000000.csv'
    
    # Check if the corresponding polar file exists in the polar folder
    polar_path = os.path.join(polar_folder, polar_filename)
    if os.path.exists(polar_path):
        # Copy the polar file to the new folder
        destination_polar_path = os.path.join(output_folder, polar_filename)
        shutil.copy(polar_path, destination_polar_path)
    else:
        print(f"Polar file for {airfoil_name} not found!")

print("Files copied successfully.")


