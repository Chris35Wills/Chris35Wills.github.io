---
layout: post
title: Reading in NetCDF data in R and exporting as a geotiff
categories: R, File I/O
tags: R, NetCDF
---

This definitely passes my "post things that took more than half an hour to work out" as I know [Aaron O'Leary](http://homepages.see.leeds.ac.uk/~eeaol/) was originally basing his posts on.

I've never had to deal with netCDF files before. They are a great way of storing lots of data and lots of variables and once you understand their structure, they are very efficient ways of distributing data. HOWEVER, if you've never had to deal with them before they are a bit of a headache.

I ended up doing this in R (and have done the equivalent now in IDL and Python which I may post soon) and have pieced the process together following "flick throughs" of R package (including [raster](http://cran.r-project.org/web/packages/raster/vignettes/Raster.pdf) and [netcdf](http://cran.r-project.org/web/packages/ncdf/ncdf.pdf)) documentation and stack exchange [threads](http://stackoverflow.com/questions/14513480/convert-matrix-to-raster-in-r) amongst other sources including [here](https://www.image.ucar.edu/GSP/Software/Netcdf/) as well as [here](http://thr3ads.net/r-help/2010/10/1040427-non-numeric-argument-to-binary-operator-error-while-reading-ncdf-file) followed by [here](http://climateaudit.org/2009/10/10/unthreaded-23/).

The first step is to install the right packages:

{% highlight R %}
#If it's the first time:
> install.packages("ncdf")
> install.packages("raster")

#If you've already got them in your library:
> library(ncdf)
> library(raster)
{% endhighlight %}

Next, you want to get your NetCDF file read and to find some summary data about it:

{% highlight R %}
> ex.nc = open.ncdf(your_path:/your_file.nc) # contains info on the .nc file but not the data
> print(ex.nc) # verbose description of the file
> summary(ex.nc) # concise summary info
{% endhighlight %} 

Assuming you know the names of the variables and attributes contained within the .nc file, you can now start pulling data out to different objects. 

In this example, we'll deal with geographic info assuming our netcdf file contains the following variables:

- proj_info 
- x_positions
- y_positions
- z_values

Let's say our "proj_info" variable contain the following attributes:

- ellipsoid
- false_easting
- false_northing
- lat_zero
- lon_zero
- lat_proj_origin

To get the variable info:

{% highlight R %}
> proj_info = get.var.ncdf( ex.nc, "proj_info", verbose=TRUE) 
> x = get.var.ncdf( ex.nc, "x", verbose=TRUE)          
> y = get.var.ncdf( ex.nc, "y", verbose=TRUE)          
> z = getx.var.ncdf( ex.nc, "z", verbose=TRUE)   
{% endhighlight %} 

If you receive an error message when trying to allocate some of this data to any of these variables saying something like:

```
"Error in mv * 1e-05 : non-numeric argument to binary operator"
```

then a fix can be found described [here]().

To get the attribute info:

{% highlight R %}
> ellipsoid = att.get.ncdf( ex.nc, "proj_info", 'ellipsoid')
> false_easting = att.get.ncdf( ex.nc, "proj_info", 'false_easting')
> false_northing = att.get.ncdf( ex.nc, "proj_info", 'false_northing') 
> lat_zero = att.get.ncdf( ex.nc, "proj_info", 'lat_zero') 
> lon_zero = att.get.ncdf( ex.nc, "proj_info", 'lon_zero')
> lat_proj_origin = att.get.ncdf( ex.nc, "proj_info", 'lat_proj_origin')
{% endhighlight %}

It would be handy for you to also print out this data to check we are reading in what we think we should be.

Now that we have our data, we can now set about creating a raster - this can be plotted to check all looks correct and the exported as a geotiff.

Firstly lets combine our x, y and z data into a list we'll conveniently call "data":

{% highlight R %}
> data=list()
> data$x=x
> data$y=y
> data$y=y
> data$z=z
> str(data)
{% endhighlight %}

We can now create a raster (which we'll call "ras") using the raster package - ignoring projection info, this can be done simply as:

{% highlight R %}
> ras = raster(data) 
{% endhighlight %}

As we have the projection info it would be useful to ensure the geotiff also contains this. By printing out the projection attributes set above (ellipsoid, false_easting and so on), you can now populate the projection variable that can be set as an input to the raster command. Here I am referring to the "CRS" variable of the [raster]() package. This takes in a string following the [proj4](http://cran.r-project.org/web/packages/proj4/proj4.pdf) syntax for which a list of variables can be found [here](https://trac.osgeo.org/proj/wiki/GenParms).

Lets assume our projection info is as follows:

> projection system = Polar Stereographic
central latitude = 71.
central longitude = -39 
false easting = 0. 
false northing = 0. 
ellipsoid = WGS1984

We can now create our raster (ras) - containing all of the required projection information - by formatting our raster function and defining the CRS variable using the correct proj4 syntax as follows:

{% highlight R %}
> ras=raster(data, crs=CRS("+proj=stere +lat_0=71. +lon_0=-39 +x_0=0. +y_0=0. +ellps=WGS1984"))
{% endhighlight %}

To export this as a geotiff - which can easily be opened in ArcGIS amongst multiple other programmes - use the following:

{% highlight R %}
> ras_out<-writeRaster(r,"your_path/your_file.tif",format="GTiff")
{% endhighlight %}

