---
layout: post
title: ENVI binary files to numpy arrays using GDAL
categories: Python Geoprocessing
tags: python, gdal, numpy, envi, raster
---

Most of my work currently revolves around raster processing of one kind or another. Being able to take advantage of the extensive 
libraries within Python (e.g. Numpy) is extremely helpful when carrying out such tasks. This [blog] (http://geoinformaticstutorial.blogspot.co.uk/2012/09/reading-raster-data-with-python-and-gdal.html) really got me onto this.

Before trying to make use of the below functions, make sure you have access to the osgeo libraries - if you don't see [here] (http://trac.osgeo.org/gdal/wiki/GdalOgrInPython).

Below is a Python function that you can take that will get any given ENVI type binary file (so long as it has a .hdr file) into a numpy array. 

{% highlight python %} 
from __future__ import division
import os
import sys

from osgeo import gdal, gdalconst 
from osgeo.gdalconst import * 


def ENVI_raster_binary_to_2d_array(file_name):
	'''
	Converts a binary file of ENVI type to a numpy array.
	Lack of an ENVI .hdr file will cause this to crash.
	'''
	
	driver.Register()

	inDs = gdal.Open(file_name, GA_ReadOnly)
	
	if inDs is None:
		print "Couldn't open this file: " + file_name
		print '\nPerhaps you need an ENVI .hdr file? A quick way to do this is to just open the binary up in ENVI and one will be created for you.'
		sys.exit("Try again!")
	else:
		print "%s opened successfully" %file_name
			
		print '~~~~~~~~~~~~~~'
		print 'Get image size'
		print '~~~~~~~~~~~~~~'
		cols = inDs.RasterXSize
		rows = inDs.RasterYSize
		bands = inDs.RasterCount
	
		print "columns: %i" %cols
		print "rows: %i" %rows
		print "bands: %i" %bands
	
		print '~~~~~~~~~~~~~~'
		print 'Get georeference information'
		print '~~~~~~~~~~~~~~'
		geotransform = inDs.GetGeoTransform()
		originX = geotransform[0]
		originY = geotransform[3]
		pixelWidth = geotransform[1]
		pixelHeight = geotransform[5]
	
		print "origin x: %i" %originX
		print "origin y: %i" %originY
		print "width: %2.2f" %pixelWidth
		print "height: %2.2f" %pixelHeight
	
		# Set pixel offset.....
		print '~~~~~~~~~~~~~~' 
		print 'Convert image to 2D array'
		print '~~~~~~~~~~~~~~'
		band = inDs.GetRasterBand(1)
		image_array = band.ReadAsArray(0, 0, cols, rows)
		image_array_name = file_name
		print type(image_array)
		print image_array.shape
		
		return image_array, pixelWidth, (geotransform, inDs)


# The function can be called as follows:
# image_array, post, envidata =  ENVI_raster_binary_to_2d_array(file_name)   image_array, post, (geotransform, inDs)
#
# Notes:
# Notice the tuple (geotransform, inDs) - this contains all of your map information (xy tie points, postings and coordinate system information)
# pixelWidth is assumed to be the same as pixelHeight in the above example, therefore representing the surface posting - if this is not the 
# case for your data then you must change the returns to suit
{% endhighlight %}  

There is a lot more you can retrun from the above function as you can see - adjust to taste. To import files of different types, have a look [here] (http://www.gdal.org/formats_list.html)
and alter the line:

{% highlight python %} 
driver = gdal.GetDriverByName('ENVI') 
{% endhighlight %}.

Once you have your numpy array and you've done some processing or whatever, it is then useful to be able to pull the array back out, exporting it 
back as an ENVI (or other) binary. A "post" input is required in case you've resampled the original imported binary through your processing. If you haven't 
resampled just pass in the original post as returned by the first function.

{% highlight python %} 
def ENVI_raster_binary_from_2d_array(envidata, file_out, post, image_array):
	util.check_output_dir(file_out)
	original_geotransform, inDs = envidata

	rows, cols = image_array.shape
	bands = 1

	# Creates a new raster data source
	outDs = driver.Create(file_out, cols, rows, bands, gdal.GDT_Float32)
	
	# Write metadata
	originX = original_geotransform[0]
	originY = original_geotransform[3]

	outDs.SetGeoTransform([originX, post, 0.0, originY, 0.0, -post])
	outDs.SetProjection(inDs.GetProjection())

	#Write raster datasets
	outBand = outDs.GetRasterBand(1)
	outBand.WriteArray(image_array)
	
	new_geotransform = outDs.GetGeoTransform()
	new_projection = outDs.GetProjection()
	
	print "Output binary saved: ", file_out
	
	return new_geotransform,new_projection,file_out
{% endhighlight %}  

Thanks to [Martin] (https://twitter.com/mewo2) for cleaning some of this up!
