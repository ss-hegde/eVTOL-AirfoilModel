"""
Arange the input data in columns [x, y, alpha, Re, M]

inputs - downsised coordinate array (x and y) and angle of attack array
outputs - elements [x, y, alpha, Re, M]
"""
import numpy as np

def organize_data(x_f, y_f, alphas):

    Elements = []

    # Loop through the polars
    for n_file in range(len(x_f)):
        x_temp = x_f[n_file]
        y_temp = y_f[n_file]
        alpha_temp = alphas[n_file]
        
        for j in range(len(alpha_temp)):
            batch = []
            # Loop through the coodrinates
            for i in range(len(x_temp)-1):
                element = np.array([x_temp[i], y_temp[i], x_temp[i+1], y_temp[i+1], alpha_temp[j]])
                # Elements.append(element)
                batch.append(element)
            batch = np.array(batch)
            batch = batch.flatten()
            Elements.append(batch)

    Elements = np.array(Elements)

    return Elements