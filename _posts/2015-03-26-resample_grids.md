---
layout: post
title: Resample raster to the size of another
categories: Python
tags: python gdal
---

The usable code is the last snippet. 

I needed to resample and resize one larger array (call it arr_src) to the
extent and post of a smaller array (arr_trgt). Using a [mesh grid](http://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html) approach,
I initially looped through the x and y grids of arr_trgt, extracting indicies
of points from the arr_src grids that were within a distance of the x and y
values representaed at a given arr_trgt position. I then averaged the z values
of arr_src at these indicies, using the mean to populate a given cell of the
resultant out grid (with an extent of arr_trgt).

The development code looked like this:

{% highlight python %}

import numpy as np

arr_src_x=np.arange(-800, 800, 70)
arr_src_in=np.arange(-3500, -600, 70)
y1,x1=np.meshgrid(y_in,x_in,indexing='ij')
z1=np.random.random(x1.shape)*100 # << your information
rows_src,cols_src=x1.shape

arr_trgt_x=np.arange(-750,580,100)
arr_trgt_y=np.arange(-3000,-400,100)
y2,x2=np.meshgrid(y2_in,x2_in,indexing='ij')
rows_trgt,cols_trgt=x2.shape

xi_good=[]
yi_good=[]
accum=np.zeros(x2.shape)

limit=200 # duistance within which coords from arr_src must be of arr_trgt)

for (y,x), value in np.ndenumerate(x2):
	
	# check coordinates are within a distance of a point
	yi_good=y1[np.logical_and(y1>=y2[y,x]-limit,y1<=y2[y,x]+limit)] 
	xi_good=x1[np.logical_and(x1>=x2[y,x]-limit,x1<=x2[y,x]+limit)] 

	# get indices of "good" coordinates
	x1_y_indx, x1_x_indx = get_index(x1, xi_good)
	y1_y_indx, y1_x_indx = get_index(y1, yi_good)

	x_x=np.unique(x1_x_indx) 
	x_y=np.unique(x1_y_indx) 

	y_x=np.unique(y1_x_indx) 
	y_y=np.unique(y1_y_indx) 

	# Average values from z1 
	accum[y,x]=np.mean(z1[y_y.min():y_y.max(),x_y.min():x_y.max()])

{% endhighlight %}

I was able to calculate my index positions using this function (with a bit of [help](http://stackoverflow.com/questions/29238782/numpy-unravel-index-not-returning-expected-row-indices)):

{% highlight python %}
def get_index(array, select_array):
	''' 
	Find the index positions of values from select_array in array
	
	Returns:
	x index array
	y index array
	'''
	mask = np.logical_or.reduce([array==val for val in np.unique(select_array)])
	y_indx, x_indx = np.where(mask)
	return y_indx, x_indx
{% endhighlight %}

However, with a arr_src of 19665 x 31573 pixels, the search in the main loop was taking ages - a result of my implemented exhasutive search approach.

Alas, I then found [this post](http://stackoverflow.com/questions/10454316/how-to-project-and-resample-a-grid-to-match-another-grid-with-gdal-python) and was able to get my code to compile and complete in seconds - thanks [gdal](http://www.gdal.org/).

{% highlight python %}
#!/usr/bin/env python

from osgeo import gdal, gdalconst

# Source
src_filename = "your_file"
src = gdal.Open(src_filename, gdalconst.GA_ReadOnly)
src_proj = src.GetProjection()
src_geotrans = src.GetGeoTransform()

# We want a section of source that matches this:
match_filename = "your_file"
match_ds = gdal.Open(match_filename, gdalconst.GA_ReadOnly)
match_proj = match_ds.GetProjection()
match_geotrans = match_ds.GetGeoTransform()
wide = match_ds.RasterXSize
high = match_ds.RasterYSize

# Output / destination
dst_filename = "your_file"
dst = gdal.GetDriverByName('GTiff').Create(dst_filename, wide, high, 1, gdalconst.GDT_Float32)
dst.SetGeoTransform( match_geotrans )
dst.SetProjection( match_proj)

# Do the work
gdal.ReprojectImage(src, dst, src_proj, match_proj, gdalconst.GRA_Bilinear)

del dst # Flush
{% endhighlight %}

