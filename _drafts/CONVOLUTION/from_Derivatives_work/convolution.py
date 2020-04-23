# -*- coding: utf-8 -*-
"""
DERIVATIVES

Moving window basecode for all derivative work
Info here: https://stackoverflow.com/questions/8174467/vectorized-moving-window-on-2d-array-in-numpy

@author: chrwil
"""


print("*************")
print("*************")
print("Developed using Python 3.6 - if you want to use arcpy make sure you have 2.7 installed (and if using anaconda, the 32-bit version")
print("*************")
print("*************")

import sys
import numpy as np

#~~~~~~
# Import custom functions
sys.path.append("W:/teams/Base_Prod/TerrainDerivatives/Github__all_scripts_and_notes/scripts/functions/")
import slope as sf
import helper as hlp
      
#~~~~~~~~~~~~~~
# Create array
arr_in = np.round(np.random.uniform(low=0, high=20, size=(11,11)), 2)
arr_out=np.ones(arr_in.shape)
arr_out2=np.ones(arr_in.shape)
assert arr_out.shape == arr_in.shape
assert arr_out2.shape == arr_in.shape

# Or use a 'real' DTM
#import arcpy
#f_in="S:/ElevationData/Bluesky_DTM/data/v1.0/DTM_5m_TIFF/HU/HU/HU15/HU1559.tif"
#arr_in=arcpy.RasterToNumPyArray(f_in)
#arr_out=np.ones(arr_in.shape)
#arr_out2=np.ones(arr_in.shape)

#~~~~~~~~~~~~~~
# Set step size and kernel size
stepsize=1
kernel_size=3 # 3x3 window
kernel_step_in=int((kernel_size-1)/2)

#~~~~~~~~~~~~~~
# Pad image to a width of (kernel size -1) /2
# Essential as the moving window needs to operate on your array corners
arr_proc=hlp.pad_array(arr_in, kernel_size=kernel_size, mode='constant', constant_values=-9999)      
  
#~~~~~~~~~~~~~~
# Create variables for progress calcualtion            
total_cells=arr_in.size
count=0

#~~~~~~~~~~~~~~
# Start loop and assign slope values
for out_i, ii in enumerate(range(0, arr_in.shape[0], stepsize)): # y
        
    for out_j, jj in enumerate(range(0, arr_in.shape[1], stepsize)): # x
                
        # Progress every 10%
        count+=1
        pcnt=int(np.round((count/total_cells)*100))
        if pcnt%5==0:
            print(int(np.round((count/total_cells)*100)), "% complete...")
    
        #arr_out[out_i, out_j] = arr_in[out_i, out_j]
        
        # Apply window function and assign value
        #   - as the array being processed is a padded version of the original, the statements 
        #   "ii+kernel_step_in" ensure the actual data is used and not the padding!
        #   - arr_out is the same size as arr_in as there is no padding.        
        arr_out[out_i, out_j]=sf.calc_slope(arr_proc, ii+kernel_step_in, jj+kernel_step_in, kernel_size, algorithm=sf.thirdOrderFD)
        arr_out2[out_i, out_j]=sf.calc_slope(arr_proc, ii+kernel_step_in, jj+kernel_step_in, kernel_size, algorithm='')
                                 
# Plot input and output
hlp.plot_orginal_vs_processed(arr_in, arr_out, cbar=True)

arr_in.min()
arr_in.max()
arr_out.min()
arr_out.max()


