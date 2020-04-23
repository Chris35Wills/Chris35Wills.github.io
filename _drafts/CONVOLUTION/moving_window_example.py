# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:09:54 2018

@author: chrwil
"""

import numpy as np
import matplotlib.pyplot as plt

# Make some toy data
arr_in = np.round(np.random.uniform(low=0, high=20, size=(11,11)), 2)
arr_out=np.ones(arr_in.shape)

# Set a kernel size (e.g. value of 3 for a 3x3 window)
kernel_size=3
#stepsize=1
#~~~~~~~~~~~~~~
# Pad image to a width of (kernel size -1) /2
# Essential as the moving window needs to operate on your array corners
arr_proc=np.pad(arr_in, int((kernel_size-1)/2), mode='constant', constant_values=-9999)

#~~~~~~~~~~~~~~
# Create some function to work on values within a kernel
def calc_slope(array, y, x, kernel_size):
    """
    """

    if array[(y,x)] != -9999.0:
        half_kernel = (kernel_size-1)//2
        subimg = array[(y - half_kernel):(y + half_kernel + 1), (x - half_kernel):(x + half_kernel + 1)]
        assert subimg.shape == (kernel_size, kernel_size), "Subimage dimensions not equal to kernel - you're probably at an edge - add padding to you array"       
        
        # Do soethign with the subimg (the extracted kernel)       
        slp_subimg=101
        return(slp_subimg)
        
    else:
        print("Move to next point")

# # Run through (and plot if True)
# for out_i, ii in enumerate(range(0, arr_in.shape[0], stepsize)): # y       
#     for out_j, jj in enumerate(range(0, arr_in.shape[1], stepsize)): # x
#         arr_out[out_i, out_j] = arr_in[out_i, out_j]
#         arr_out[out_i, out_j] = calc_slope(arr_in, ii, jj, kernel_size)

# 
# 

stepsize=1
for out_i, ii in enumerate(range(0,arr_proc.shape[0]-1, stepsize)): # y       
    for out_j, jj in enumerate(range(0, arr_proc.shape[1]-1, stepsize)): # x
        print(out_i, out_j)
        arr_out[out_i, out_j] = arr_in[out_i, out_j]


        arr_out[out_i, out_j] = arr_in[out_i, out_j]
        arr_out[out_i, out_j] = calc_slope(arr_in, ii, jj, kernel_size)
        


# Plot output      
f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)
ax1.imshow(arr_in)
ax1.set_title(title1)
ax2.imshow(arr_out)
ax2.set_title(title2)
plt.show()



##~~~~~ OTHER CONVOLUTION IDEAS
##~~~~~~~~~~~~
##~~~~~~~~~~~~~~~~~~~
##import time
##import scipy.signal
##import astropy
## Moving window using convolve from astropy...
#print("See here: http://docs.astropy.org/en/stable/api/astropy.convolution.convolve.html#astropy.convolution.convolve")
##~~~~~~~~~~~~~~~~~~~
## More moving window links here:
#print("https://community.esri.com/blogs/dan_patterson/2017/11/15/rolling-statistics-for-grid-data-an-alternative")
#print("https://community.esri.com/blogs/dan_patterson/2017/11/26/filter-convolve-rolling-sliding")
##~~~~~~~~~~~~~~~~~~~
## Moving window using convolve from scipy...
## See here: https://stackoverflow.com/questions/8174467/vectorized-moving-window-on-2d-array-in-numpy
#A =np.round(np.random.random_sample((1111,1111)),2)
#B = np.ones((3,3))/4
#tic = time.clock()
#C_no_pad = scipy.signal.convolve2d(A,B,mode='same')#,'fft')
#C_pad = scipy.signal.convolve2d(A,B,mode='valid', boundary='fill', fillvalue=0)#,'fft')
#toc = time.clock()
#print("That took ", toc-tic, "seconds")
#plot_comparison(C_no_pad, C_pad, title1="Unpadded", title2="Padded")
#print("WARNING")
#print("For convolution in scipy, you have to reverse the kernel - look at convolution using the astropy package for a more intuitve implementation")
#print("Also read this: https://stackoverflow.com/questions/40247760/scipy-convolve2d-outputs-wrong-values")
