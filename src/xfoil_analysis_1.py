"""
Perform XFOIL aalysis on the airfoil coordinate files stored in a directory and 
provide airfoil polars as output.

Author: Sharath Hegde
Date: 25.08.2024
"""

# COMMENTS - 
# This code has problems with analyzing the airfoils.
# For certain conditions convergence issues arise. It has nothing to do with the code
# It is because of the xfoil package.
# This code can be run only in WSL environment

from xfoil import XFoil
from xfoil.model import Airfoil
# from xfoil.test import naca0012
import matplotlib.pyplot as plt
import csv
import numpy as np
import os

# Parameters
Re = 1e6
min_alpha = -20.0
max_alpha = 20.0
alpha_intervals = 0.25
niter = 200

# Function to run xfoil on airfoil coordinates
def xfoil_analysis(airfoil_coordinates, Re, iter, min_alpha, max_alpha, alpha_intervals, output_csv):
    xf = XFoil()
    xf.airfoil = Airfoil(airfoil_coordinates[:,0], airfoil_coordinates[:,1])

    xf.Re = Re
    xf.max_iter = iter

    a, cl, cd, cm, cp = xf.aseq(min_alpha, max_alpha, alpha_intervals)

    # Saving the results to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Alpha', 'Cl', 'Cd', 'Cm'])
        for i in range(len(a)):
            csvwriter.writerow([a[i], cl[i], cd[i], cm[i]])

    return a, cl, cd

# Directory where files are saved
# save_directory = "airfoil_coordinate_database"
save_directory = "temp_database/"

for filename in os.listdir(save_directory):

    print("Processing: ", filename)

    airfoil_name = filename
    airfoil_coordinates = np.loadtxt(save_directory+airfoil_name, skiprows=1)

    # print(airfoil_coordinates[:, 0])
    # print(airfoil_coordinates[:, 1])   
    
    if filename.endswith("_coordinates.dat"):
        # Load airfoil coordinates from a .dat file
        airfoil_name = (os.path.splitext(filename)[0]).split('_')[0]
        airfoil_coordinates = np.loadtxt(save_directory+'/'+filename, skiprows=1)
        # print(airfoil_coordinates)

        alpha, lift_coeff, drag_coeff = xfoil_analysis(airfoil_coordinates=airfoil_coordinates,
                                                        Re=Re, iter=niter, min_alpha=min_alpha, max_alpha=max_alpha, alpha_intervals=alpha_intervals,
                                                          output_csv=save_directory+'xf-'+airfoil_name+'-il-'+str(int(Re))+'.csv')
        
        plt.plot(alpha, lift_coeff)
        plt.show()



# alpha, lift_coeff, drag_coeff = xfoil_analysis(airfoil_coordinates=airfoil_coordinates, Re=1e6, iter=40, output_csv='xf-'+airfoil_name+'-il-'+str(int(Re))+'.csv')

# plt.plot(alpha, lift_coeff)
# plt.show()