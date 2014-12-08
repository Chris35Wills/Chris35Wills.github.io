---
layout: post
title: Installing gdal binaries for Python on a windows machine 
categories: Python 
tags: python, gdal
---

The [gdal](http://www.gdal.org/) library is an excellent source of tools that help you query, process and manipulate spatial data of varying formats. It can be used directly from the command line in both linux and windows environments and is also accessible through its own windows command line set up, downloaded [here](http://trac.osgeo.org/osgeo4w/).

Some particularly useful tools I've found are:

>gdal_translate		
>gdalinfo		
>gdal_warp		

which let you: convert between raster formats, list info relating to a given raster and reproject raster data respectively.

To use it with Python - assuming that python is already installed and you know which version you have - you require the gdal bindings which can be downloaded [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal). If you have windows 7 and Python version 2.7, then you want to scroll down to the GDAL list and run GDAL-1.11.1.win-amd64-py2.7.exe

Importing the gdal library into your python environment is then possible using:

{% highlight python %} 
from osgeo import gdal, gdalconst 
from osgeo.gdalconst import * 
{% endhighlight %} 

An example of its application can be seen in [this](http://chris35wills.github.io/python-gdal-raster-io/) post. 