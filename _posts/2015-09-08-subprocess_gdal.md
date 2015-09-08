---
layout: post
title: Calling gdal utilities from within python using subprocess
categories: Python, gdal
tags: python gdal geospatial raster
---

I am always using [gdal commands in python](https://pcjericks.github.io/py-gdalogr-cookbook/). Sometimes though there are things that just happen faster though using the OSgeo4W Shell (I'm using windows at the moment) such as gdal_translate. It is still possible to use these commands within a given python script - it just requires use of the subprocess package, and in the case of using commands specific to the OSGeo4W shell, a python call to a given script from inside the OSGeo4W shell.

Say I have a geotiff called terrain.tif and I want to convert it to an ESRI ASCII format, within a script, I just need the following:

{% highlight python %}
import subprocess

subprocess.call('gdal_translate -ot FLOAT32 -of AAIGrid terrain.tif terrain.asc', shell=True)
{% endhighlight %}

I can then open the resultant file as normal and continue along with the script i.e. I never have to step out of the script to run the gdal_translate function externally.

[More info here](https://pymotw.com/2/subprocess/)