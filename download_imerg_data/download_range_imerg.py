from datetime import datetime
import time
from servir.utils.download_data import get_gpm_files, initialize_event_folders
from servir.utils.m_tif2h5py import tif2h5py
import h5py
import matplotlib.pyplot as plt
import os
import sys

#give it the path to the folder where you want to save the data 

if len(sys.argv) != 4:
    print("Usage: python download_range_imerg.py <folder_path> <start_date> <end_date>")
    print("Example: python download_range_imerg.py path/to/data/ 2010-04-02 2010-04-02")
    sys.exit(1)

folder_name = sys.argv[1]
start_date_str = sys.argv[2]
end_date_str = sys.argv[3]

output_folder = str(folder_name) 
# Set your date range (YYYY-MM-DD)
initial_timestamp = f"{start_date_str} 00:00:00"
final_timestamp = f"{end_date_str} 23:30:00"

# Convert to datetime objects
initial_timestamp = datetime.strptime(initial_timestamp, "%Y-%m-%d %H:%M:%S")
final_timestamp = datetime.strptime(final_timestamp, "%Y-%m-%d %H:%M:%S")

# Set domain and output folder
xmin, xmax, ymin, ymax = -21.4, 30.4, -2.9, 33.1
req_shape = (360, 518)
#  Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Download .tif files for the date range (timing this step)
ppt_server_path = 'https://jsimpsonhttps.pps.eosdis.nasa.gov/imerg/gis/early/'
email = 'aaravamudan2014@my.fit.edu'
req_height, req_width = req_shape

print("Starting IMERG data download...")
start_time = time.time()
get_gpm_files(output_folder, initial_timestamp, final_timestamp, ppt_server_path, email, req_height, req_width)
end_time = time.time()
elapsed = end_time - start_time
print(f"IMERG download completed in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")

# Convert all .tif files in the folder to a single .h5 file
meta_fname = output_folder + 'metadata.json'
h5_fname = output_folder + 'imerg_data.h5'
tif2h5py(tif_directory=output_folder, h5_fname=h5_fname, meta_fname=meta_fname, x1=xmin, y1=ymin, x2=xmax, y2=ymax)

print(f"Saved H5 file: {h5_fname}")

# Show number of samples, shape, and plot the first image
with h5py.File(h5_fname, 'r') as h5f:
    if 'precipitations' in h5f:
        data = h5f['precipitations']
        data1=h5f['timestamps']
        print("#####################################################")
        print(f"Dataset 'precipitations' shape: {data.shape}")
        print(f"Number of samples (timesteps): {data.shape[0]}")
        print("#####################################################")
        

        print(f"first timestamp: {data1[0]}")
        print(f"last timestamp: {data1[-1]}")
        print("#####################################################")
        # Show the first image or whatever you want to do with the data
        # plt.imshow(data[0], cmap='Blues')
        # plt.title("First IMERG Precipitation Image")
        # plt.colorbar(label='Precipitation (mm/hr)')
        # plt.show()
       
    else:
        print("Could not find 'precipitations' dataset in the H5 file. Available datasets:", list(h5f.keys()))
        
        
        