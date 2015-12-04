---
layout: post
title: Gridding data
categories: Python
tags: python grid numpy
---


'''
Grid data to a specific resolution 
Find positions withion the grid relative to round xy coordinates - populate rounded position with value
Find and return index of max position in array
'''

import numpy as np

df = pd.read_csv("xyz_data.txt", sep = "\s*", header=None, names=["x","y","z","time"])

x=df["x"].values # array pos 0
y=df["y"].values # array pos 1
z=df["z"].values # array pos 2
time=df["time"].values # array pos 3

x_250m = np.ones([3001,5601]) ## x array
y_250m = np.ones([3001,5601]) ## y array
mean_250m = np.ones([3001,5601]) ## Prior known dimensions of data
points_250m = np.ones([3001,5601]) ## number of points
con_250m = np.ones([3001,5601]) ## value or not conditional

### Repeat this for all lines of df:
for i in range(len(df)):
	
	# extract first line of data as indexed array
	data = df.iloc[i,:]

	# data projected relative to a false easting of -300000 - this sets the easting to zero
	x_250m_t=(data[0]+300000.)/250.
	# data projected relative to a false easting of -2400000 - this sets the northing to zero
	y_250m_t=(data[1]+2400000.)/250. 

	# populate array with positions - these will accumulate
	x_250m[np.round(x_250m_t),np.round(y_250m_t)] = means_250m[np.round(x_250m_t),np.round(y_250m_t)] + data[0] 
	y_250m[np.round(x_250m_t),np.round(y_250m_t)] = means_250m[np.round(x_250m_t),np.round(y_250m_t)] + data[1] 

	# populate array at rounded position with elevation - this will accumulate...
	means_250m[np.round(x_250m_t),np.round(y_250m_t)] = means_250m[np.round(x_250m_t),np.round(y_250m_t)] + data[2] 

	# accumulates the number of "hits" per cell (used later on to calc the mean)
	points_250m[np.round(x_250m_t),np.round(y_250m_t)] = means_250m[np.round(x_250m_t),np.round(y_250m_t)] + 1

	# Boolean/layer to ID if values exist within square
	con_250m[np.round(x_250m_t),np.round(y_250m_t)] = 1

## Calculates mean arrays
x_250m = x_250m/points_250m # mean x pos
y_250m = y_250m/points_250m # mean y pos
means_250m = means_250m/points_250m # mean elev - EVENLY GRIDDED

## Get position of max
means_250m.argmax(axis=0)
i,j = np.unravel_index(means_250m.argmax(), means_250m.shape)
max = means_250m[i,j]
print "Max: %f, Max_x: %i, Max_y: %i" %(max, i, j)

'''
The con_250m surface could then be used to work out which parts of the grid still need populating
'''