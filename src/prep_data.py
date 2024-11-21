"""
Read the airfoil coordinate file and the polar file and extract the following data as arrays - 
x coordinates, y coordinates, C_l, C_d, C_m, angle of attack
"""

import os
import numpy as np
import re
import pandas as pd

def prep_data(root, keyword=None):

    # Initialization of arrays
    # Coordinates
    x_i = [] # Initial coordinates - before downsizing
    y_i = []

    # Polars
    alphas = []
    Cls = []
    Cds = []
    Cms = []

    if keyword:
        # lists of files in each dir
        coord_files = [f for f in os.listdir(root) if f == (keyword+'_coordinates.dat')]
        polar_files = [f for f in os.listdir(root) if f == ('xf-'+keyword+'-il-1000000.csv')]
    else:
        # lists of files in each dir
        coord_files = [f for f in os.listdir(root) if f.endswith('_coordinates.dat')]
        polar_files = [f for f in os.listdir(root) if f.endswith('.csv')]

    # Extract base names from coordinate files
    coord_bases = {re.sub(r'\_coordinates.dat$', '', f) for f in coord_files}
    polar_bases = {}
    for polar_file in polar_files:
        match = re.match(r'xf-(.*)-il-1000000\.csv$', polar_file)
        if match:
            base_name = match.group(1)
            polar_bases[base_name] = polar_file

    for base_name in coord_bases:
        if base_name in polar_bases:
            coord_file = f"{base_name}_coordinates.dat"
            polar_file = polar_bases[base_name]

            coordinate_data = np.loadtxt(root+coord_file)
            # polar_data = np.loadtxt(root+polar_file, skiprows=12)
            polar_data = pd.read_csv(root+polar_file, skiprows=10)
            polar_data = polar_data[(polar_data['Alpha'] >= -2) & (polar_data['Alpha'] <= 10)]

            # Coordinates
            x = []
            y = []

            # Polars
            alpha = polar_data['Alpha'].values
            Cl = polar_data['Cl'].values
            Cd = polar_data['Cd'].values
            Cm = polar_data['Cm'].values


            for i in range(0, len(coordinate_data)):
                np.array(x.append(float(coordinate_data[i][0]))) 
                np.array(y.append(float(coordinate_data[i][1])))
                
            if len(x) >= 35:    # Only consider the files with more than 35 coordinates
                x_i.append(x)
                y_i.append(y)

                alphas.append(alpha)

                for num_val in range(len(Cl)):
                    Cls.append(Cl[num_val])
                    Cds.append(Cd[num_val])
                    Cms.append(Cm[num_val])
                        
    return x_i, y_i, Cls, Cds, Cms, alphas