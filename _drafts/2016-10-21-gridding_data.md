---
layout: post
title: Creating a DEM from irregular or regularly spaced points
---

DEMs (raster format) are created from point elevation observations. When working with a DEM, it is important to be aware that the values of a given cell are the result of some processing step that converted point elevations to a value at that location. Point data can be regularly (e.g. every 10 m along north and east directions) or irregularly spaced (i.e. all over the place). Different approaches are taken to convert these points to a DEM raster. 

Unless you have all of the information regarding how a DEM was created (including estimates of uncertainty), you can only be truly confident in the values of a DEM if you do the point to raster conversion yourself. This is often glosssed over. 

This process can be carried out using various tools (python, gdal etc.) but I find the most succinct approach is to use the excellent libraries from R, namley [raster]() and [sp](). 

Note that there is a difference between interpolating a surface from points (this interpolates values at gaps where observations are not available), and createing a gridded representation of a point dataset (where data are not available, a grid cell shouldn't have a value). 

## Regularly gridded points

### Example

### R

	https://cran.r-project.org/web/packages/raster/raster.pdf
	rasterFromXYZ

### Python 

COPIED STRAIGHT FROM: http://stackoverflow.com/questions/30764955/python-numpy-create-2d-array-of-values-based-on-coordinates

Assuming the x and y values in your file directly correspond to indices (as they do in your example), you can do something similar to this:

	import numpy as np

	x = [0, 0, 1, 1, 2, 2]
	y = [1, 2, 0, 1, 1, 2]
	z = [14, 17, 15, 16, 18, 13]

	z_array = np.nan * np.empty((3,3))
	z_array[y, x] = z

	print z_array

Which yields:

	[[ nan  15.  nan]
	 [ 14.  16.  18.]
	 [ 17.  nan  13.]]

For large arrays, this will be much faster than the explicit loop over the coordinates.

If you have regularly sampled x & y points, then you can convert them to grid indices by subtracting the "corner" of your grid (i.e. x0 and y0), dividing by the cell spacing, and casting as ints. You can then use the method above or in any of the other answers.

As a general example:

i = ((y - y0) / dy).astype(int)
j = ((x - x0) / dx).astype(int)

grid[i,j] = z

## Irregularly gridded points

### Example

Often, your data won't be regularly spaced. Now you need to consider methods specically dealing with this, including regularly gridding the data yourself (which will include averaging or some  sort of function) - what if multiple points fall within the area of a raster cell?

### R Code

Using R, irregular points can be converted to a grid using R's [raster]() package (rasterize)[] function. 

	library(raster)
	library(sp)

	path="O:/Documents/CHRIS_Bristol/Bathymetry_data/Fenty_ALLOWED/2013-2014 Rignot and others bathymetry/2013-2014 Rignot and others bathymetry/"
	f<-capture.output(cat(path, "2014_Greenland_Rignot-Weinreibe-Cofaigh_Nash_DiskoBay_100m_UTM84-22N_m.xyz", sep=""))
	pts <- read.table(f, header=FALSE, col.names=c("x", "y", "z"))
	names(pts)
	ncol(pts)
	class(pts)

	# create a SpatialPointsDataFrame
	coordinates(pts) = ~x+y # create a spatialPoints data frame

	# create an empty raster object to the extent of the points
	rast <- raster(ext=extent(pts), resolution=250)

	# create your output raster
	rasOut<-rasterize(pts, rast, pts$z, fun = mean)
	image(rasOut)

	#write it out
	fout=capture.output(cat(path, "rignot_bathym_mean_grid_250m.tif"))
	writeRaster(rasOut, fout, format="GTiff")

### Python equiv...

See "Dealing with non-uniform x & y input" on http://stackoverflow.com/questions/30764955/python-numpy-create-2d-array-of-values-based-on-coordinates


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NOTES....


#####
#######
#########
###########
#Python
#http://gis.stackexchange.com/questions/116319/plotting-elevation-maps-and-shaded-relief-images-from-latitude-longitude-and-e

import glob
import numpy as np
import matplotlib.mlab as ml
import pandas as pd

dat=glob.glob("O:/Documents/CHRIS_Bristol/Bathymetry_data/Fenty_ALLOWED/2013-2014 Rignot and others bathymetry/2013-2014 Rignot and others bathymetry/*.xyz")
post = 1000
#df_lnd = pd.read_csv(dat[0], sep = "\s*", skiprows=5, header=None, names=['x','y','z']) 
df = pd.read_csv(dat[0], sep = "\s*", header=None, names=['x','y','z']) 
x = df['x'].values
y = df['y'].values
z = df['z'].values

##Mesh Grid
xi = np.linspace(min(x), max(x), post)
yi = np.linspace(min(y), max(y), post)
YY, XX = np.meshgrid(yi, xi,indexing='ij')

##Grid data (using linear interpolation) - will also populate cells outsoide of the points so will require masking
ZZ = ml.griddata(x, y, z, xi, yi, interp='linear')
#ZZ = ml.griddata(x, y, z, xi, yi)

plt.imshow(ZZ, origin='lower')
plt.colorbar()
plt.show()



# write out geotiff




#####
#######
#########
###########
#GDAL
#http://www.gdal.org/grid_tutorial.html



#####
#######
#########
###########
#R
#http://www.maths.lancs.ac.uk/~rowlings/Teaching/UseR2012/cheatsheet.html

######################
# Raster pacakge: rasterize (for irregular points)

# http://gis.stackexchange.com/questions/79062/how-to-make-raster-from-irregular-point-data-without-interpolation
s100 <- matrix(c(267573.9, 2633781, 213.29545, 262224.4, 2633781, 69.78261, 263742.7, 2633781, 51.21951, 259328.4, 2633781, 301.98413, 264109.8, 2633781, 141.72414, 255094.8, 2633781, 88.90244),  ncol=3,  byrow=TRUE)
colnames(s100) <- c('X', 'Y', 'Z')

library(raster)
# set up an 'empty' raster, here via an extent object derived from your data
e <- extent(s100[,1:2])
e <- e + 1000 # add this as all y's are the same

r <- raster(e, ncol=10, nrow=2)

# or r <- raster(xmn=, xmx=,  ...

# you need to provide a function 'fun' for when there are multiple points per cell
x <- rasterize(s100[, 1:2], r, s100[,3], fun=mean)
plot(x)

##### --- or--- #####

#http://gis.stackexchange.com/questions/24588/converting-point-data-into-gridded-dataframe-for-histogram-analysis-using-r
library(raster)
pts <- read.csv("IP.csv")
coordinates(pts) <- ~lat+lon
rast <- raster(ncol = 10, nrow = 10)
extent(rast) <- extent(pts)
rasterize(pts, rast, pts$IP, fun = mean)


######################
# Raster package: rasterFromXYZ (for regular points)

	# https://cran.r-project.org/web/packages/raster/raster.pdf
	# rasterFromXYZ


###################### Another approach... you have to make the point regular first
# Number 1 : Regularly grid points

	# Regular grid
	#http://stackoverflow.com/questions/14335585/converting-irregular-grid-to-regular-grid

# Number 2 : Use raster packages rasterFromXYZ function

	# rasterFromXYZ
	# https://cran.r-project.org/web/packages/raster/raster.pdf
	
