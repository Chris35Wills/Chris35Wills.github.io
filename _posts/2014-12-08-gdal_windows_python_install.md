---
layout: post
title: Installing gdal binaries for Python on a windows machine 
categories: Python 
tags: python, gdal
---

The [gdal](http://www.gdal.org/) library is an excellent source of tools that help you query, process and manipulate spatial data of varying formats. It can be used directly from the command line in both linux and windows environments and is also accessible through its own windows command line set up, downloaded [here](http://trac.osgeo.org/osgeo4w/).

Some particularly useful tools I've found are:

>gdal_translate		convert between raster formats

>gdalinfo		list info relating to a given raster 

>gdal_warp		reproject raster data

To use it with Python - assuming that python is already installed and you know which version you have - you require the gdal bindings which can be downloaded [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal).

Importing the gdal library into your python environment is then possible using:

{% highlight python %} 
from osgeo import gdal, gdalconst 
from osgeo.gdalconst import * 
{% endhighlight %} 

An example of its application can be seen in [this](http://chris35wills.github.io/python-gdal-raster-io/) post. 