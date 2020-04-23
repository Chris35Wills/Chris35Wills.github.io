#~~~~~~~~~~~~~~~~~~~~
# Plot position of moving window over base array (needs optimising)
#   1. make an array
#   2. loop over the array with a moving window
#   3. plot the moving window over the base array
import numpy as np
import matplotlib.pyplot as plt
import copy

stepsize=1
kernel_size=3
arr_in = np.round(np.random.uniform(low=0, high=20, size=(9,9)), 2)
arr_clean=copy.deepcopy(arr_in)

plt.imshow(arr_in)
for out_i, ii in enumerate(range(0, arr_in.shape[0], stepsize)): # y      
    for out_j, jj in enumerate(range(0, arr_in.shape[1], stepsize)): # x
      
#arr_in[ii:ii+kernel_size, jj:jj+kernel_size]=100              
#plt.imshow(arr_in)
#arr_in[ii+stepsize:(ii+kernel_size)+stepsize, jj+stepsize:(jj+kernel_size)+stepsize]=200              
#plt.imshow(arr_in)

        while (ii<arr_in.shape[0] and jj<arr_in.shape[1]) and (ii>arr_in.shape[0] and jj>arr_in.shape[1]): # assumes step of 1
            # moving window
            arr_in[ii+kernel_size, jj+kernel_size]=100              
            plt.imshow(arr_in)
            plt.pause(0.06)

            # overlapping window (by one step)
            arr_in[(ii+kernel_size)+stepsize, (jj+kernel_size)+stepsize]=200              
            plt.imshow(arr_in)
            plt.pause(0.06)

        arr_in=arr_clean