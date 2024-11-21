"""
Download the airfoil coordinate files from UIUC databse
Author: Sharath Hegde
Date: 25.08.2024
"""

from bs4 import BeautifulSoup
import re
import urllib.request as urllib
import os

# Directory where files will be saved
save_directory = "airfoil_coordinate_database"

# Ensure the directory exists
os.makedirs(save_directory, exist_ok=True)

# Base URLs
baseFlpth1 = "https://m-selig.ae.illinois.edu/ads/coord/"
baseFlpth2 = "https://m-selig.ae.illinois.edu/ads/coord_updates/"

# Open and read the HTML page
html_page = urllib.urlopen("https://m-selig.ae.illinois.edu/ads/coord_database.html")
soup = BeautifulSoup(html_page, 'lxml')

ind = 1

for link in soup.find_all('a', attrs={'href': re.compile('\.dat', re.IGNORECASE)}):
    # file_name = link.get('href').rsplit('/', 1)[-1]
    # file_url = baseFlpth1 + file_name

    original_file_name = link.get('href').rsplit('/', 1)[-1]
    
    # Modify the file name to include '_coordinates'
    base_name, ext = os.path.splitext(original_file_name)
    # new_file_name = f"{base_name}_coordinates{ext}"
    new_file_name = f"{base_name}_coordinates{ext}"
    
    file_url = baseFlpth1 + original_file_name

    # Try the primary URL first, then the secondary URL if the file is not found
    try:
        urllib.urlretrieve(file_url, os.path.join(save_directory, new_file_name))
    except urllib.HTTPError:
        file_url = baseFlpth2 + original_file_name
        try:
            urllib.urlretrieve(file_url, os.path.join(save_directory, new_file_name))
        except urllib.HTTPError as e:
            print(f"Failed to retrieve {file_url}: {e}")

    print(f"Saving file {ind}")
    ind += 1
